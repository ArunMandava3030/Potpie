from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_service import process_document

# Initialize the router for document-related endpoints
router = APIRouter()

# Define the route to process documents
@router.post("/api/documents/process")
async def process_document_endpoint(file: UploadFile = File(...)):
    try:
        # Process the document using the service function
        asset_id = process_document(file.file)
        return {"asset_id": asset_id}
    except Exception as e:
        # Return an error if something goes wrong
        raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")
