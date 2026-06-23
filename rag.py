from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

from langchain_qdrant import QdrantVectorStore

# HuggingFace Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Ollama LLM
llm = ChatOllama(
    model="qwen2.5:latest",
    temperature=0.3
)


def process_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(pages)

    vector_store = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        path="./qdrant_data",
        collection_name="pdf_collection"
    )

    return vector_store


def ask_question(vector_store, query):

    docs = vector_store.similarity_search(
        query,
        k=4
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a PDF Assistant.

Answer ONLY using the provided PDF context.

Context:
{context}

Question:
{query}

If the answer is not found in the PDF, say:
"I could not find this information in the uploaded PDF."
"""

    response = llm.invoke(prompt)

    return response.content, docs