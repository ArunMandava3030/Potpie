from chromadb import Client
from chromadb.config import Settings
from app.config import VECTOR_DB_PATH

# Initialize ChromaDB client
def get_vector_db():
    client = Client(Settings(path=VECTOR_DB_PATH))
    return client
