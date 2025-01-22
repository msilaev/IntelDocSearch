from typing import List, Any
import numpy as np
import pinecone  # Assuming Pinecone is used as the vector database

class VectorDB:
    def __init__(self, index_name: str):
        self.index_name = index_name
        pinecone.init(api_key='YOUR_API_KEY', environment='YOUR_ENVIRONMENT')
        self.index = pinecone.Index(index_name)

    def upsert_embeddings(self, embeddings: List[tuple]):
        """Store document embeddings in the vector database."""
        self.index.upsert(vectors=embeddings)

    def query_embeddings(self, query_vector: List[float], top_k: int = 5) -> List[dict]:
        """Retrieve the top_k most similar document embeddings."""
        response = self.index.query(queries=[query_vector], top_k=top_k)
        return response['matches']

    def delete_embeddings(self, ids: List[str]):
        """Delete embeddings from the vector database by their IDs."""
        self.index.delete(ids=ids)

    def close(self):
        """Close the connection to the vector database."""
        pinecone.deinit()