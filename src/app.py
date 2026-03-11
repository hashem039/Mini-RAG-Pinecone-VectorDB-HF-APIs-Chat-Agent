import streamlit as st
from rag_pipeline import generate_answer
from pdf_utils import extract_text_from_pdf
from ingest import ingest_text

st.title("Mini-RAG Chatbot (Hugging Face)")

# ----------------------
# SIDEBAR PDF UPLOAD
# ----------------------

st.sidebar.header("Upload PDF")

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file:

    st.sidebar.success("PDF uploaded")

    if st.sidebar.button("Add to Knowledge Base"):

        with st.sidebar.spinner("Processing document..."):

            text = extract_text_from_pdf(uploaded_file)

            chunks = ingest_text(text, uploaded_file.name)

        st.sidebar.success(f"Indexed {chunks} chunks!")

# ----------------------
# CHAT SYSTEM
# ----------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask a question")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = generate_answer(prompt)

        st.write(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )