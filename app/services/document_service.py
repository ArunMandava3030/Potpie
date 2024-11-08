import uuid
from app.database.vector_store import get_vector_db
from app.embeddings.embedder import create_embeddings

def process_document(file_path: str):
    # Read file content
    with open(file_path, 'r') as file:
        content = file.read()
        
    # Create embeddings
    embeddings = create_embeddings(content)
    
    # Generate unique asset ID
    asset_id = str(uuid.uuid4())
    
    # Store in vector database
    vector_db = get_vector_db()
    vector_db.add_documents([{"id": asset_id, "text": content, "embedding": embeddings}])
    
    return asset_id
