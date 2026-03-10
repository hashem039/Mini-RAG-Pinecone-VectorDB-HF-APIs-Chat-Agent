import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
HF_TOKEN = os.getenv("HF_API_KEY")

INDEX_NAME = "mini-rag"

# Pinecone setup
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

# Hugging Face API info
HF_API_URL = "https://router.huggingface.co/v1/chat/completions"
HF_HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}
HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2:featherless-ai"