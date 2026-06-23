import streamlit as st
import tempfile

from rag import process_pdf, ask_question

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="PDF AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# CSS
# -------------------------
st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#0f172a,
#1e293b,
#312e81,
#7c3aed
);
}

.main-title{
text-align:center;
font-size:3rem;
font-weight:700;
color:white;
}

.sub-title{
text-align:center;
font-size:1.1rem;
color:#d1d5db;
margin-bottom:20px;
}

[data-testid="stSidebar"]{
background:#111827;
}

.stButton button{
background:#7c3aed;
color:white;
border:none;
border-radius:12px;
font-weight:bold;
}

.stButton button:hover{
background:#8b5cf6;
}

.source-card{
padding:15px;
border-radius:15px;
background:rgba(255,255,255,0.08);
margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown("""
<div class="main-title">
🤖 PDF AI Assistant
</div>

<div class="sub-title">
Powered by Ollama + HuggingFace Embeddings + Qdrant
</div>
""", unsafe_allow_html=True)

# -------------------------
# SESSION STATE
# -------------------------
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = ""

# -------------------------
# SIDEBAR
# -------------------------
with st.sidebar:

    st.title("📚 Control Panel")

    if st.session_state.pdf_name:
        st.success(
            f"Loaded PDF:\n{st.session_state.pdf_name}"
        )

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("""
### Features

✅ PDF Upload

✅ Local AI (Ollama)

✅ Chat History

✅ Source References

✅ Qdrant Vector Search

✅ HuggingFace Embeddings
""")

# -------------------------
# FILE UPLOAD
# -------------------------
uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    st.session_state.pdf_name = uploaded_file.name

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        tmp_file.write(
            uploaded_file.read()
        )

        pdf_path = tmp_file.name

    if st.button("🚀 Process PDF"):

        with st.spinner(
            "Processing PDF..."
        ):

            st.session_state.vector_store = process_pdf(
                pdf_path
            )

        st.success(
            "PDF Processed Successfully!"
        )

# -------------------------
# CHAT HISTORY
# -------------------------
for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):
        st.write(
            msg["content"]
        )

# -------------------------
# CHAT INPUT
# -------------------------
if st.session_state.vector_store:

    query = st.chat_input(
        "Ask anything about the PDF..."
    )

    if query:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": query
            }
        )

        with st.chat_message("user"):
            st.write(query)

        with st.spinner("Thinking..."):

            answer, docs = ask_question(
                st.session_state.vector_store,
                query
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message(
            "assistant"
        ):
            st.write(answer)

        with st.expander(
            "📄 Source Chunks"
        ):

            for i, doc in enumerate(docs):

                page = doc.metadata.get(
                    "page",
                    "Unknown"
                )

                st.markdown(
                    f"### 📄 Page {page + 1}"
                    if isinstance(page, int)
                    else "### 📄 Page Unknown"
                )

                st.markdown(
                    f"""
<div class="source-card">
{doc.page_content[:1500]}
</div>
""",
                    unsafe_allow_html=True
                )

else:

    st.info(
        "Upload a PDF and click Process PDF to start chatting."
    )