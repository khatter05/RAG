import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain.document_loaders import UnstructuredMarkdownLoader
import chromadb
from app.config import DATA_PATH, EMBEDDING_MODEL, CHROMA_DB_PATH
from app.utils import log_info, log_error

def load_documents() -> list:
    """Loads markdown documents and splits them into chunks."""
    loader = UnstructuredMarkdownLoader(DATA_PATH)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=60)
    return text_splitter.split_documents(documents)

# Initialize Ollama embeddings
embedding_function = OllamaEmbeddings(model=EMBEDDING_MODEL)

def embeddings_exist() -> bool:
    """Checks if ChromaDB contains valid embeddings, not just the folder."""
    if os.path.exists(CHROMA_DB_PATH) and os.listdir(CHROMA_DB_PATH):
        client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        collection = client.get_or_create_collection(name="chroma")
        
        # Check if embeddings are actually stored
        if collection.count() > 0:
            log_info(f"Existing embeddings detected in {CHROMA_DB_PATH}. Skipping generation.")
            return True
        else:
            log_info("ChromaDB found, but no embeddings exist. Regenerating.")
    
    log_info("No existing embeddings found. Proceeding with generation.")
    return False


def generate_embeddings(chunks: list) -> list:
    """Generates embeddings only if they are not already stored in ChromaDB."""
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    collection = client.get_or_create_collection(name="chroma")

    if embeddings_exist():
        log_info("Loading existing embeddings from ChromaDB...")
        stored_embeddings = []
        for idx in range(collection.count()):
            result = collection.get(ids=[str(idx)], include=['embeddings'])
            stored_embeddings.append(result['embeddings'][0])
        log_info("Loaded embeddings successfully.")
        return stored_embeddings
    
    log_info("Generating new embeddings...")
    from concurrent.futures import ThreadPoolExecutor
    
    with ThreadPoolExecutor() as executor:
        embeddings = list(executor.map(lambda chunk: embedding_function.embed_query(chunk.page_content), chunks))
    
    log_info("Embeddings generated successfully.")
    return embeddings

# ChromaDB Setup
def setup_chroma(chunks: list, embeddings: list):
    """Creates or loads a ChromaDB collection, ensuring persistence."""
    try:
        log_info(f"Initializing ChromaDB at: {CHROMA_DB_PATH}")
        client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        collection = client.get_or_create_collection(name="chroma")

        if collection.count() == 0:
            log_info("Adding new embeddings to ChromaDB...")
            for idx, chunk in enumerate(chunks):
                collection.add(
                    documents=[chunk.page_content], 
                    metadatas=[{'id': idx}], 
                    embeddings=[embeddings[idx]], 
                    ids=[str(idx)]
                )
            log_info(f"Added {len(chunks)} documents to ChromaDB.")
        else:
            log_info("Embeddings already exist. Using stored data.")

    except Exception as e:
        log_error(f"Error in ChromaDB setup: {str(e)}")

    return client, collection
