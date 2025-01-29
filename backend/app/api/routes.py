from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel

from ..services.search_service import SearchService
from ..services.summarization_service import SummarizationService
from ..services.embedding_service import EmbeddingService
import fitz
import os

router = APIRouter()
embedding_service = EmbeddingService()

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5  # Default value for top_k

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with fitz.open(file_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text += page.get_text()
    return text


@router.get("/")
async def start():
    return f"Welcome to the Intelligent Document Search API!"
    

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    try:
        file_location = f"app/uploads/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        with open(file_location, "wb") as file_object:
            file_object.write(await file.read())
        
        print("Uploaded file:", file_location)
        if file.filename.endswith('.pdf'):
            text = extract_text_from_pdf(file_location) 
        else:
            content = await file.read()
            text = content.decode('utf-8')
        
        embeddings = embedding_service.generate_embeddings(text)
        embedding_service.store_embeddings(file.filename, embeddings)
        
        # Here you would typically save the document and process it
        return {"filename": file.filename, "content_type": file.content_type}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/search/")
async def search(request: SearchRequest):
    try:       
        print("try") 
        results = embedding_service.search_embeddings(request.query, top_k=request.top_k)
        print("results")
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/summarize/")
async def summarize(file: UploadFile = File(...)):
    try:
        content = await file.read()
        summary = SummarizationService(content)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))