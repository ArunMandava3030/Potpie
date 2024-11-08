### **Project Overview**

The Document Chatbot API project is a FastAPI-based service that allows users to upload documents, process them, and generate embeddings. These embeddings are useful for querying documents or generating responses based on the document's content. This setup can be the foundation for a chatbot that interacts with users based on the data within uploaded documents.

---

### **Project Structure**

Here's a high-level directory structure and purpose of each component in the project:

```
document_chatbot/
├── app/
│   ├── main.py                   # Main entry point for the FastAPI application
│   ├── routers/
│   │   ├── documents.py           # Defines API endpoints related to document processing
│   │   └── chat.py                # Defines API endpoints related to chat functionalities
│   ├── services/
│   │   ├── document_service.py     # Service layer handling document processing logic
│   ├── embeddings/
│   │   └── embedder.py            # Embeddings logic, integrates with LangChain
├── myenv/                         # Virtual environment (optional, not usually pushed to Git)
└── requirements.txt               # Lists required dependencies for the project
```

---

### **Directory and File Descriptions**

1. **`app/main.py`**:
   - This is the main application file where the FastAPI app is initialized.
   - It includes two routers: `documents` and `chat`, which handle document processing and chat-based interactions, respectively.
   - It also contains a root route (`/`) that returns a welcome message, and it runs the server when executed directly.

2. **`app/routers/documents.py`**:
   - Defines the API endpoint `/api/documents/process`, which handles file uploads for document processing.
   - When a document is uploaded, it calls the `process_document` function from `document_service.py` to generate an embedding or handle other document processing tasks.

3. **`app/routers/chat.py`**:
   - Contains routes for chat functionalities (such as generating responses based on document content).
   - The endpoint uses embeddings to create relevant responses based on user queries.

4. **`app/services/document_service.py`**:
   - Contains the core logic for handling uploaded documents. This file includes the `process_document` function, which generates embeddings or processes the document content as required.
   - Acts as a service layer, keeping the business logic separated from API routing.

5. **`app/embeddings/embedder.py`**:
   - Uses the LangChain library to create embeddings of documents via `OpenAIEmbeddings`.
   - Manages embeddings creation for documents, which enables similarity searches and content-based responses.

6. **`requirements.txt`**:
   - Contains the list of all required dependencies, such as FastAPI, Uvicorn, and LangChain.
   - This file is essential for setting up the project environment on a new machine.

---

### **How the Project Works**

1. **Uploading Documents**:
   - Users upload a document through the `/api/documents/process` endpoint.
   - The document's contents are processed, and embeddings are generated, allowing the chatbot to "understand" the document context for future interactions.

2. **Generating Responses (Chat)**:
   - Users can interact with the chatbot using endpoints in the `chat.py` router.
   - The chatbot uses pre-processed embeddings to generate context-aware responses, allowing it to respond based on the uploaded document's content.

3. **Embedding with LangChain**:
   - The embeddings are created using LangChain's `OpenAIEmbeddings` module, which translates document content into vector representations. These vectors are later used to match user queries with relevant document sections.

---

### **Steps to Run the Project**

Follow these steps to set up and run the project locally.

#### 1. **Clone the Project Repository**

   ```bash
   git clone https://github.com/ArunMandava3030/Potpie.git
   cd Potpie
   ```

#### 2. **Set Up a Virtual Environment**

   (Optional but recommended)
   ```bash
   python -m venv myenv
   source myenv/bin/activate         # On macOS/Linux
   myenv\Scripts\activate            # On Windows
   ```

#### 3. **Install Dependencies**

   Ensure `requirements.txt` is in the project root, then install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### 4. **Run the FastAPI Server**

   Start the server using Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```
   - The server will be available at `http://127.0.0.1:8000`.
   - The `--reload` flag allows auto-reloading when you make code changes.

#### 5. **Test the Endpoints**

   Use **Postman** or **cURL** to test endpoints.

   - **Root Endpoint**:
     ```bash
     GET http://127.0.0.1:8000/
     ```
     Expected Response:
     ```json
     {
       "message": "Welcome to the Document Chatbot API"
     }
     ```

   - **Document Upload Endpoint**:
     Use Postman to send a POST request to `http://127.0.0.1:8000/api/documents/process` with a document file in the `file` field.

#### 6. **Check Embeddings/Chat Functionality**

   - Once the document is processed, embeddings are stored or used for querying.
   - Use the chat endpoints in `chat.py` to query based on document embeddings.

---

### **Final Notes*

- **Environment Variables**: For real-world applications, sensitive data (such as API keys) should be stored in environment variables or a `.env` file.
- **Embedding Caching**: In production, embeddings may need to be cached or saved in a database for faster querying.
![Screenshot 2024-11-08 193215](https://github.com/user-attachments/assets/558f3ba5-27c9-4ca3-923f-372728d55271)
![Screenshot 2024-11-08 193958](https://github.com/user-attachments/assets/c9efa78a-6f7a-429f-bb40-fbc9f9c2d1f2)

