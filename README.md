# Mini-RAG Chatbot with Hugging Face & Pinecone

A Retrieval-Augmented Generation (RAG) system designed to answer questions from your documents. This project uses semantic search via Pinecone to find relevant context and Hugging Face's LLM API to generate accurate, context-aware answers.

---

## 🚀 Features
- **Vector Search:** High-speed semantic retrieval using Pinecone.
- **Local Embeddings:** SentenceTransformers (`all-MiniLM-L6-v2`) for private document representation.
- **LLM Power:** Mistral-7B-Instruct (via Hugging Face API) for high-quality generation.
- **Interactive UI:** Streamlit web interface for chat and dynamic PDF ingestion.
- **AI-Optimized:** Includes `GEMINI.md` for seamless integration with AI development agents.

---

## 🏗️ Project Structure
```text
/
├── src/
│   ├── app.py           # Streamlit chat & upload UI
│   ├── config.py        # API keys & client initialization
│   ├── ingest.py        # Logic to process text/PDFs into Pinecone
│   ├── rag_pipeline.py  # Retrieval + HF generation logic
│   ├── rag_utils.py     # Embeddings & chunking utilities
│   └── pdf_utils.py     # PDF parsing logic
├── data/                # Local documents for ingestion
├── .github/             # GitHub Actions workflows (CI/CD)
├── GEMINI.md            # AI Agent instructions (Internal)
├── requirements.txt     # Python dependencies
└── .env.example         # Environment variable template
```

---

## 🛠️ Setup Instructions

### 1. Prerequisites (Pinecone)
Create a Pinecone index with the following parameters:
- **Name:** `mini-rag`
- **Dimension:** 384
- **Metric:** `cosine`

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/hashem039/Mini-RAG-Pinecone-VectorDB-HF-APIs-Chat-Agent.git
cd Mini-RAG-Pinecone-VectorDB-HF-APIs-Chat-Agent

# Create and activate virtual environment
python -m venv .hmenv
source .hmenv/bin/activate  # Linux/Mac
# .hmenv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment
Copy `.env.example` to `.env` and fill in your API keys:
```bash
cp .env.example .env
```
**Required Keys:**
- `PINECONE_API_KEY`: Your Pinecone project key.
- `HF_API_KEY`: Your Hugging Face User Access Token.
- `GEMINI_API_KEY`: (Optional) Required for Gemini CLI integration.

---

## 📖 Usage

### Start the Chat App
Launch the Streamlit interface to interact with your data:
```bash
streamlit run src/app.py
```

### Ingesting Documents
- **Via UI:** Use the sidebar in the Streamlit app to upload and index PDFs dynamically.
- **Via CLI:** Place `.txt` files in the `data/` folder and run the ingestion script:
  ```bash
  python src/ingest.py
  ```

---

## 🤖 AI-Assisted Development
This repository is optimized for use with the **Gemini CLI**. See [GEMINI.md](./GEMINI.md) for detailed architectural context and instructions used by AI agents to help you develop, review, and maintain this codebase.

---

## 🧪 CI / CD
This project includes a GitHub Actions workflow (`.github/workflows/test-and-lint.yml`) that automatically runs:
- **Pylint:** Static analysis on `src/`.
- **Pytest:** Unit tests (if present).

To run locally:
```bash
pip install pylint pytest
pylint src || true
pytest -q
```
