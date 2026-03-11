import uuid
from config import index
from rag_utils import embed_text, chunk_text


def load_document():
    with open("document.txt") as f:
        return f.read()


def ingest():
    text = load_document()
    chunks = chunk_text(text)

    vectors = []

    for chunk in chunks:
        vectors.append({
            "id": str(uuid.uuid4()),
            "values": embed_text(chunk),
            "metadata": {"text": chunk}
        })

    index.upsert(vectors=vectors)
    print(f"Inserted {len(vectors)} chunks.")


def ingest_text(text, source="uploaded_document"):

    chunks = chunk_text(text)

    vectors = []

    for i, chunk in enumerate(chunks):
        vectors.append({
            "id": str(uuid.uuid4()),
            "values": embed_text(chunk),
            "metadata": {
                "text": chunk,
                "source": source,
                "chunk_id": i
            }
        })

    index.upsert(vectors=vectors)

    return len(vectors)


if __name__ == "__main__":
    ingest()