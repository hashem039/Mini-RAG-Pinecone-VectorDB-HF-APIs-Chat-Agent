# Gemini CLI Context: Mini-RAG Chatbot (Hugging Face & Pinecone)

This project is a Retrieval-Augmented Generation (RAG) system built with Python, using Pinecone for vector storage, SentenceTransformers for embeddings, and Hugging Face's Chat API for answer generation.

## Project Overview

*   **Architecture:** Modular RAG pipeline (Ingestion -> Retrieval -> Generation).
*   **Key Technologies:**
    *   **Frontend:** Streamlit (`src/app.py`)
    *   **Vector Database:** Pinecone (`src/config.py`, `src/ingest.py`)
    *   **Embeddings:** `all-MiniLM-L6-v2` via SentenceTransformers (`src/rag_utils.py`)
    *   **LLM:** `Mistral-7B-Instruct-v0.2` via Hugging Face Inference API (`src/rag_pipeline.py`)
    *   **PDF Parsing:** `pypdf` (`src/pdf_utils.py`)

## Directory Structure

*   `src/`: Core logic (app, config, ingest, rag_pipeline, rag_utils, pdf_utils).
*   `tests/`: Unit test suite using `pytest`.
*   `data/`: Local source documents.
*   `prompts/`: Reference prompts for development and testing.

## Building and Running

### 1. Environment Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest pytest-mock  # For testing
```

### 2. Running the Application
*   **Web Interface:** `streamlit run src/app.py`
*   **Manual Ingestion:** `python src/ingest.py`

### 3. Testing
Execute the test suite using `pytest`. Mocks are used to avoid requiring API keys or heavy dependencies during testing.
```bash
export PYTHONPATH=$PYTHONPATH:./src
pytest tests
export PYTHONPATH=$PYTHONPATH:.

## Development Conventions

*   **RAG Parameters:** `TOP_K = 10`, `SIMILARITY_THRESHOLD = 0.75`, `chunk_size = 500`, `overlap = 100`.
*   **Testing:** All new features must include unit tests in the `tests/` directory with appropriate mocking of external services.
*   **Imports:** Use absolute imports from `src` or ensure `src` is in the `PYTHONPATH`.
