import requests
from config import index, HF_API_URL, HF_HEADERS, HF_MODEL
from rag_utils import embed_text

TOP_K = 10
SIMILARITY_THRESHOLD = 0.75

def retrieve_context(question):
    vector = embed_text(question)
    results = index.query(
        vector=vector,
        top_k=TOP_K,
        include_metadata=True
    )
    return results["matches"]

def filter_context(context):
    """
    Filter and aggregate matched context chunks based on a similarity threshold.
    This function expects `context` to be an iterable (e.g., list) of match
    dictionaries where each match has at least the following structure:
        {
            "score": <numeric similarity score>,
            "metadata": {"text": <string chunk>}
        }
    Behavior:
    - Collects the "text" field from each match whose "score" is greater than or
      equal to the global SIMILARITY_THRESHOLD and returns them as a single string
      with chunks joined by newline characters.
    - If no matches meet the threshold, the function attempts a fallback by
      taking the first three items from a variable named `matches` and returning
      their metadata text joined by newlines.
    Parameters:
    - context (Iterable[dict]): Iterable of match dictionaries to filter.
    Returns:
    - str: A newline-joined string of filtered (or fallback) text chunks.
    Notes:
    - The function relies on a global constant SIMILARITY_THRESHOLD to decide
      which chunks to keep.
    - The current fallback references a variable named `matches` which is not
      defined within the function. If the fallback path is taken and `matches`
      does not exist in the enclosing scope, a NameError will be raised.
      Consider changing the fallback to use the provided `context` (e.g.,
      context[:3]) or ensure `matches` is defined in the calling scope.
    Raises:
    - NameError: may be raised if the fallback branch is executed and `matches`
      is not defined in scope.
    """

    filtered_chunks = []

    for match in context:
        score = match["score"]
        print(f"Score: {score}")

        if score >= SIMILARITY_THRESHOLD:
            filtered_chunks.append(match["metadata"]["text"])

    # fallback if nothing passes threshold
    if not filtered_chunks:
        filtered_chunks = [m["metadata"]["text"] for m in context[:3]]

    context = "\n".join(filtered_chunks)
    return context

def generate_answer(question):
    context = retrieve_context(question)
    context = filter_context(context)

    prompt = f"Answer the question using the context below:\n\nContext:\n{context}\n\nQuestion:\n{question}"

    payload = {
        "model": HF_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_new_tokens": 200,
        "max_tokens": 1000
    }

    try:
        response = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload).json()
    except Exception as e:
        return f"Error calling Hugging Face API: {e}"

    # Robust handling for HF response
    if "error" in response:
        return f"API Error: {response['error']}"
    
    # HF chat endpoint returns 'generation' list under 'choices' or directly under 'message'
    try:
        # New HF format: response["choices"][0]["message"]["content"]
        return response["choices"][0]["message"]["content"]
    except KeyError:
        # fallback for older or different response format
        try:
            return response["generations"][0]["text"]
        except (KeyError, IndexError):
            return f"Unexpected API response: {response}"