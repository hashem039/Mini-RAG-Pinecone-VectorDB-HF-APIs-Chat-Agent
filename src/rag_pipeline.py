import requests
from config import index, HF_API_URL, HF_HEADERS, HF_MODEL
from rag_utils import embed_text

def retrieve_context(question):
    vector = embed_text(question)
    results = index.query(
        vector=vector,
        top_k=3,
        include_metadata=True
    )
    return "\n".join([m["metadata"]["text"] for m in results["matches"]])

def generate_answer(question):
    context = retrieve_context(question)

    prompt = f"Answer the question using the context below:\n\nContext:\n{context}\n\nQuestion:\n{question}"

    payload = {
        "model": HF_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_new_tokens": 200
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