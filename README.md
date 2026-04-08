# Mini-RAG Chatbot with Hugging Face & Pinecone

This project implements a Retrieval-Augmented Generation (RAG) system designed to answer questions from documents. It uses semantic search to find relevant context and a Large Language Model (LLM) to generate accurate answers.

---

## Overview
This setup is ideal for learning RAG pipelines or building small AI assistants.

* Pinecone: Vector database for high-speed semantic search.
* SentenceTransformers: Local embeddings for document representation.
* Hugging Face Chat API: State-of-the-art LLM for generating answers.
* Streamlit: Web-based interface for chat and **dynamic PDF uploads.

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
├── data/                 # Local documents to ingest
├── docs/                 # Documentation and diagrams
├── src/                  # Main source code
│   ├── app.py            # Streamlit chat & upload UI
│   ├── config.py         # API keys, Pinecone & HF setup
│   ├── ingest.py         # Logic to process PDFs and text into Vector DB
│   ├── rag_pipeline.py   # Retrieval + HF generation logic
│   ├── rag_utils.py      # Embeddings & chunking utilities
│   └── pdf_utils.py      # PDF parsing and extraction logic
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
Use the Sidebar to upload a PDF. The system will automatically:
Extract text via pdf_utils.py.
Process and chunk the data via ingest.py.
Upsert embeddings to your Pinecone Vector DB.

or 

Place any text files in the data/ folder and run the ingestion script:

python src/ingest.py

This chunks your documents, generates embeddings, and uploads them to your Pinecone index.

### 2. Start the Chat App
Launch the Streamlit interface to interact with your data:

streamlit run src/app.py

Once documents are ingested, use the Streamlit chat interface to ask questions based on your uploaded content.

---

## CI / CD (GitHub Actions)
This repository includes a GitHub Actions workflow at `/.github/workflows/ci-cd.yml` that runs static analysis and tests on
pull requests and pushes to `main`.

What the workflow does

- Installs project dependencies from `requirements.txt` (if present).
- Installs `pylint` and `pytest` and runs them.
    - `pylint` runs over `src/` (or `app/`), or falls back to linting all tracked `.py` files.
    - `pytest` runs when a `tests/` directory or test files are present.

Notes for maintainers

- No external secrets are required by this workflow — it only runs lint and tests.
- By default the workflow is permissive for lint failures (it won't block the job). If you prefer lint failures to fail the CI job, remove the `|| true` guard in the `pylint` step in the workflow file.

Local checks before pushing

Run the following locally to match CI behavior:

```powershell
# Create/activate virtualenv (Windows PowerShell)
python -m venv .hmenv
. .\hmenv\Scripts\Activate.ps1

# Install project deps (optional)
pip install -r requirements.txt

# Install tools
pip install pylint pytest

# Run pylint (adjust target to your source dir)
pylint src || true

# Run tests
pytest -q
```

