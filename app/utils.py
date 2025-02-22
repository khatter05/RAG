import logging
from app.config import LOG_FILE

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_info(message: str) -> None:
    """Logs an info message."""
    logging.info(message)

def log_error(message: str) -> None:
    """Logs an error message."""
    logging.error(message)
