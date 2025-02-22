import os

# Directories
DATA_PATH = "data/context/text.md"
CHROMA_DB_PATH = "data/database/"

# Model names
EMBEDDING_MODEL = "mxbai-embed-large"
CHAT_MODEL = "deepseek-r1"

# Logging
LOG_DIR = "logs/"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Ensure directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(CHROMA_DB_PATH, exist_ok=True)
