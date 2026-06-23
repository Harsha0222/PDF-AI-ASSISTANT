# 📚 PDF AI Assistant

A powerful PDF Question Answering application built with Streamlit, Ollama, HuggingFace Embeddings, and Qdrant.

Upload any PDF and chat with it using AI. The application retrieves relevant information from the document and generates accurate answers using Retrieval-Augmented Generation (RAG).

## 🚀 Features

- 📄 Upload PDF documents
- 🤖 Chat with your PDFs
- 🔍 Semantic Search using Vector Embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 Interactive Chat Interface
- 📚 Source Chunk References
- 🎨 Modern Vibrant UI
- 🏠 Fully Local AI using Ollama
- ⚡ Fast Vector Search with Qdrant


## 🛠️ Tech Stack

### Frontend
- Streamlit

### LLM
- Ollama
- Qwen 2.5

### Embeddings
- HuggingFace Embeddings
- all-MiniLM-L6-v2

### Vector Database
- Qdrant

### PDF Processing
- PyPDF

## 📂 Project Structure

```bash
rag-pdf/
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
│
├── qdrant_data/
├── venv/
└── __pycache__/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/rag-pdf.git

cd rag-pdf
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🤖 Install Ollama

Download Ollama:

https://ollama.com/download

Verify Installation:

```bash
ollama --version
```

## 📥 Pull Qwen Model

```bash
ollama pull qwen2.5
```

Verify:

```bash
ollama list
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

## 📖 Usage

### Step 1

Upload a PDF file.

### Step 2

Click:

```text
🚀 Process PDF
```

### Step 3

Ask questions such as:

```text like
What is AI?

Summarize this document.

What is the main topic?

Explain chapter 3.
```

### Step 4

View AI-generated answers along with source references.

## 🔥 Future Enhancements

- Multi-PDF Support
- Chat History Persistence
- Citation Highlighting
- Voice Input
- Export Chat to PDF
- Dark / Light Theme Toggle
- Hybrid Search (BM25 + Vector Search)

---

## 👨‍💻 Author

Karnati Harsha Vardhan

GitHub: https://github.com/Harsha0222