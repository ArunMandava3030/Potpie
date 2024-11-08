from langchain.embeddings import OpenAIEmbeddings

from app.config import EMBEDDING_MODEL_NAME

def create_embeddings(text):
    # Initialize the embeddings model
    embedding_model = OpenAIEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    return embedding_model.embed_text(text)
