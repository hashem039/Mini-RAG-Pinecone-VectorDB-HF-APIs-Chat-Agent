# Gemini CLI Context: Mini-RAG Chatbot (Hugging Face & Pinecone)

This project is a Retrieval-Augmented Generation (RAG) system built with Python, using Pinecone for vector storage, SentenceTransformers for embeddings, and Hugging Face's Chat API for answer generation. It features a Streamlit-based web interface for chat and PDF document ingestion.

## Project Overview

*   **Architecture:** Modular RAG pipeline consisting of ingestion, retrieval, and generation phases.
*   **Key Technologies:**
    *   **Frontend:** [Streamlit](https://streamlit.io/) (`src/app.py`)
    *   **Vector Database:** [Pinecone](https://www.pinecone.io/) (`src/config.py`, `src/ingest.py`)
    *   **Embeddings:** `all-MiniLM-L6-v2` via [SentenceTransformers](https://www.sbert.net/) (`src/rag_utils.py`)
    *   **LLM:** `Mistral-7B-Instruct-v0.2` via [Hugging Face Inference API](https://huggingface.co/docs/api-inference/index) (`src/rag_pipeline.py`)
    *   **PDF Parsing:** `pypdf` (`src/pdf_utils.py`)

## Directory Structure

*   `src/`: Main source code directory.
    *   `app.py`: Streamlit application entry point (UI and orchestration).
    *   `config.py`: Environment variable loading and client initialization (Pinecone, HF).
    *   `ingest.py`: Logic for chunking and upserting document vectors to Pinecone.
    *   `rag_pipeline.py`: Core RAG logic (similarity search + prompt construction + LLM call).
    *   `rag_utils.py`: Text embedding and chunking utilities.
    *   `pdf_utils.py`: PDF text extraction helper.
*   `data/`: Local directory for source documents (e.g., `document.txt`).
*   `.env.example`: Template for required API keys (`PINECONE_API_KEY`, `HF_API_KEY`).

## Building and Running

### 1. Environment Setup
```bash
python -m venv .hmenv
source .hmenv/bin/activate  # Linux/Mac
# .hmenv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 2. Configuration
Create a `.env` file from `.env.example` and provide:
*   `PINECONE_API_KEY`
*   `HF_API_KEY` (Hugging Face User Access Token)

### 3. Running the Application
*   **Web Interface:** `streamlit run src/app.py`
*   **Manual Ingestion:** `python src/ingest.py` (Ingests `data/document.txt`)

### 4. Testing and Linting
```bash
pylint src || true
pytest -q
```

## Development Conventions

*   **RAG Parameters:**
    *   `TOP_K = 10` (Number of chunks to retrieve).
    *   `SIMILARITY_THRESHOLD = 0.75` (Threshold for relevant context filtering).
    *   `chunk_size = 500`, `overlap = 100` for text splitting.
*   **Prompting:** Context-aware prompts are constructed in `src/rag_pipeline.py` using a strictly defined template.
*   **Error Handling:** Robust handling for Hugging Face API responses (e.g., handling both `choices` and `generations` keys).
*   **CI/CD:** GitHub Actions workflow in `.github/workflows/test-and-lint.yml` runs `pylint` and `pytest`.

## Usage Tips

*   **PDF Uploads:** Use the Streamlit sidebar to upload and index PDFs dynamically.
*   **Vector Search:** If no chunks meet the similarity threshold, the system falls back to the top 3 matches.
*   **Embeddings:** Local embedding generation ensures no document content is sent to an external embedding API.
