from app.retrieval import retrieve_context
from app.query import query_deepseek
from app.utils import log_info

def ask_question(question: str) -> str:
    """Handles the entire workflow from retrieval to response."""
    log_info(f"User asked: {question}")
    
    context = retrieve_context(question)
    thinking, answer = query_deepseek(question, context)

    log_info(f"Generated response: {answer}")
    return answer
