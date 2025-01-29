from sentence_transformers import SentenceTransformer
import pinecone
import os
import numpy as np
from dotenv import load_dotenv

from pinecone import Pinecone, ServerlessSpec

load_dotenv()
pc = Pinecone(
        api_key=os.environ.get("PINECONE_API_KEY")
    )   

pinecone_key = os.getenv("PINECONE_API_KEY")

class EmbeddingService:

    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):

        self.model = SentenceTransformer(model_name)
        self.pc = Pinecone(api_key=pinecone_key)
    # Create the index if it doesn't exist
        if 'document-embeddings' not in self.pc.list_indexes().names():
            self.pc.create_index(
                name='document-embeddings',
                dimension=384,  # Adjust the dimension based on your model
                metric='euclidean',
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )

        self.index = self.pc.Index('document-embeddings')

    def generate_embeddings(self, text: str):
        embeddings = self.model.encode(text)
        print(text)
        print(f"Generated embeddings: {embeddings[:5]}...")  # Print first 5 values for debugging
        return embeddings
        
    def store_embeddings(self, doc_id: str, embeddings: np.ndarray):
        try:
            print(f"Storing embeddings for document ID: {doc_id}")
            embeddings_list = embeddings.astype(np.float32).flatten().tolist()  # Fix typo here

            #   Ensure correct format for upsert
            self.index.upsert(vectors=[(doc_id, embeddings_list)])

            print("Embeddings stored successfully")
        except Exception as e:
            print(f"Failed to store embeddings: {e}")


    def search_embeddings(self, query: str, top_k: int = 5):
        query_embedding = self.generate_embeddings(query)
        return self.index.query(query_embedding, top_k=top_k)

    
# Example usage:
# embedding_service = EmbeddingService()
# embeddings = embedding_service.generate_embeddings("Sample text")
# embedding_service.store_embeddings("doc_1", embeddings)