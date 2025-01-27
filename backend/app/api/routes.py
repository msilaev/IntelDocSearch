from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from ..services.search_service import SearchService
from ..services.summarization_service import SummarizationService

router = APIRouter()

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    try:
        content = await file.read()
        # Here you would typically save the document and process it
        return {"filename": file.filename, "content_type": file.content_type}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/search/")
async def search(query: str):
    try:
        results = SearchService(query)
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