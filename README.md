# Mini-RAG Chatbot with Hugging Face & Pinecone

This project implements a Retrieval-Augmented Generation (RAG) system designed to answer questions from documents. It uses semantic search to find relevant context and a Large Language Model (LLM) to generate accurate answers.

---

## Overview
This setup is ideal for learning RAG pipelines or building small AI assistants.

* Pinecone: Vector database for high-speed semantic search.
* SentenceTransformers: Local embeddings for document representation.
* Hugging Face Chat API: State-of-the-art LLM for generating answers.
* Streamlit: Simple, web-based chat interface.

---

## Prerequisites: Pinecone Setup
Before running the application, you must create a Pinecone index on the cloud with the following parameters:

```python
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="YOUR_PINECONE_API_KEY")

pc.create_index(
    name="mini-rag",
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)

## Project Structure

mini-rag-hf/
├── data/                 # Documents to ingest (e.g., document.txt)
├── docs/                 # Documentation and diagrams
├── src/                  # Main source code
│   ├── app.py            # Streamlit chat UI
│   ├── config.py         # API keys, Pinecone & HF setup
│   ├── ingest.py         # Document ingestion script
│   ├── rag_pipeline.py   # Retrieval + HF generation logic
│   └── rag_utils.py      # Embeddings & chunking utilities
├── tests/                # Unit tests
├── .env.example          # Template for environment variables
├── requirements.txt      # Project dependencies
├── setup.py              # Optional pip-installable project
└── pyproject.toml        # Modern Python metadata

---

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/yourusername/mini-rag-hf.git
cd mini-rag-hf

### 2. Create a Virtual Environment
python -m venv .hmenv

# Linux/Mac
source .hmenv/bin/activate

# Windows
.hmenv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Configure Environment Variables
Copy .env.example to .env and fill in your API keys:

cp .env.example .env

Required Keys:
* PINECONE_API_KEY: Your Pinecone project key.
* HF_TOKEN: Your Hugging Face User Access Token.

---

## Usage

### 1. Ingest Documents
Place any text files in the data/ folder and run the ingestion script:

python src/ingest.py

This chunks your documents, generates embeddings, and uploads them to your Pinecone index.

### 2. Start the Chat App
Launch the Streamlit interface to interact with your data:

streamlit run src/app.py