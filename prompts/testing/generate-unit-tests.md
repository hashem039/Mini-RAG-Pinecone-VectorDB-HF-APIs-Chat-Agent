# Prompt: Generate Unit Tests for RAG Pipeline

## Role
Act as a Senior QA Engineer specializing in Python and AI/ML applications.

## Context
This project is a Retrieval-Augmented Generation (RAG) system using Pinecone, Hugging Face, and Streamlit. The codebase is organized in `src/`.

## Task
Generate a comprehensive suite of unit tests using `pytest`.

## Constraints & Requirements
1. **Mocking:** You MUST use `unittest.mock` or `pytest-mock` to mock all calls to:
   - `pinecone.Index`
   - `requests.post` (Hugging Face API)
   - `pypdf.PdfReader`
2. **Coverage Targets:**
   - `src/rag_utils.py`: Test `chunk_text` with various sizes and overlaps.
   - `src/rag_pipeline.py`: Test `filter_context` for both success (above threshold) and fallback (below threshold) cases.
   - `src/pdf_utils.py`: Test extraction from a mocked PDF stream.
   - `src/ingest.py`: Test the `ingest_text` flow to ensure it correctly calls the embedding and upsert functions.
3. **Architecture:**
   - Provide a `tests/conftest.py` for shared fixtures (e.g., a mock Pinecone index).
   - Ensure tests are modular and easy to run with a simple `pytest` command.
4. **Style:** Follow PEP 8 and use descriptive test function names.

## Output
Provide the full file content for each new test file.
