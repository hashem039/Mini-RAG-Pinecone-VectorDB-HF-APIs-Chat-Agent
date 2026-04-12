# Prompt: Refactor RAG Pipeline Logic

## Role
Act as a Senior Backend Engineer and AI Architect.

## Context
The current RAG pipeline is in `src/rag_pipeline.py`. It handles retrieval, context filtering, and generation.

## Task
Refactor the code to improve modularity, error handling, and performance.

## Constraints
1. **Abstractions:** Move context filtering into a separate class or utility if it simplifies `generate_answer`.
2. **Error Handling:** Add more granular error handling for network timeouts and API rate limits.
3. **Logging:** Integrate Python's `logging` module instead of `print` statements.
4. **Compatibility:** Ensure the changes do not break the Streamlit interface in `src/app.py`.
