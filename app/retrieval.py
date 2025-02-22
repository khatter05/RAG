from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from app.embeddings import setup_chroma, load_documents, generate_embeddings
from app.config import CHROMA_DB_PATH, EMBEDDING_MODEL
from app.utils import log_info

# Setup ChromaDB
chunks = load_documents()
embeddings = generate_embeddings(chunks)
client, collection = setup_chroma(chunks, embeddings)

# Initialize embedding function correctly
embedding_function = OllamaEmbeddings(model=EMBEDDING_MODEL)  # ✅ Corrected

# Initialize retriever
retriever = Chroma(
    collection_name="chroma",
    client=client,
    embedding_function=embedding_function  # ✅ Corrected
).as_retriever()

def retrieve_context(question: str) -> str:
    """Retrieves relevant context from stored embeddings."""
    results = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in results])
    
    log_info(f"Context retrieved for question: {question}")
    return context
