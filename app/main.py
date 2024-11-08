from fastapi import FastAPI
from app.routers import documents, chat
import uvicorn

# Initialize FastAPI application
app = FastAPI()

# Include the router for documents and chat
app.include_router(documents.router)
app.include_router(chat.router)

# Root route to test if the server is working
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Document Chatbot API"}

# Entry point for the app if executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
