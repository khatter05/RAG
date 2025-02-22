import re
from langchain_community.llms import Ollama
from app.config import CHAT_MODEL
from app.utils import log_info

# Initialize DeepSeek-R1
deepseek_llm = Ollama(model=CHAT_MODEL)

def query_deepseek(question: str, context: str) -> tuple:
    """Formats input and queries DeepSeek-R1."""
    formatted_prompt = f"Question: {question}\n\nContext: {context}"
    response = deepseek_llm.invoke(formatted_prompt)

    # Extract <think>...</think> and final answer
    think_match = re.search(r'<think>(.*?)</think>', response, flags=re.DOTALL)
    thinking_process = think_match.group(1).strip() if think_match else "No explicit thinking process provided."
    final_answer = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL).strip()
    
    log_info(f"Model queried successfully for: {question}")
    return thinking_process, final_answer
