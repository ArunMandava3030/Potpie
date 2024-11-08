import os

VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./data/vector_db")
EMBEDDING_MODEL_NAME = "openai_text_embedding"  # replace with the chosen embedding model
