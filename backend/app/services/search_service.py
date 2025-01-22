from typing import List, Dict
from fastapi import HTTPException
from .utils.vector_db import VectorDB
from .models.document import Document

class SearchService:
    def __init__(self, vector_db: VectorDB):
        self.vector_db = vector_db

    def search_documents(self, query: str) -> List[Dict]:
        try:
            # Retrieve relevant document embeddings based on the query
            relevant_docs = self.vector_db.search(query)
            return relevant_docs
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_document_by_id(self, doc_id: str) -> Document:
        try:
            document = self.vector_db.get_document(doc_id)
            if not document:
                raise HTTPException(status_code=404, detail="Document not found")
            return document
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))