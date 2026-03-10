from pinecone import Pinecone, ServerlessSpec

## Run this once to create the index in Pinecone.
pc = Pinecone(api_key="")

pc.create_index(
    name="mini-rag",
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)