from sentence_transformers import SentenceTransformer
import pinecone
import os
import numpy as np
import sqlite3
from dotenv import load_dotenv

from pinecone import Pinecone, ServerlessSpec

load_dotenv()
pc = Pinecone(
        api_key=os.environ.get("PINECONE_API_KEY")
    )   

pinecone_key = os.getenv("PINECONE_API_KEY")

class EmbeddingService:

    def __init__(self, model_name: str = 'all-MiniLM-L6-v2', db_path: str = 'documents.db'):

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
        self.db_path = db_path
        self._create_documents_table()

    def _create_documents_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                doc_id TEXT PRIMARY KEY,
                text TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def generate_embeddings(self, text: str):
        embeddings = self.model.encode(text)        
        return embeddings
        
    def store_embeddings(self, doc_id: str, embeddings: np.ndarray, text: str):
        try:
            #print(f"Storing embeddings for document ID: {doc_id}")
            embeddings_list = embeddings.astype(np.float32).flatten().tolist()  # Fix typo here

            #   Ensure correct format for upsert
            self.index.upsert(vectors=[(doc_id, embeddings_list)])

             # Store document text in the database
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO documents (doc_id, text) VALUES (?, ?)", (doc_id, text))
            conn.commit()
            conn.close()

            print("Embeddings stored successfully")
        except Exception as e:
            print(f"Failed to store embeddings: {e}")

    def get_document_text(self, doc_id: str) -> str:
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT text FROM documents WHERE doc_id = ?", (doc_id,))
            row = cursor.fetchone()
            conn.close()
            if row:
                return row[0]
            else:
                return ""
        except Exception as e:
            print(f"Failed to retrieve document text: {e}")
            return ""

    def search_embeddings(self, query: str, top_k: int = 5):
        try:
            query_embedding = self.generate_embeddings(query)
            #print(f"Query embedding: {query_embedding[:5]}...")  # Print first 5 values for debugging
            results = self.index.query(vector=query_embedding.tolist(), top_k=top_k)  # Use keyword arguments
            #print(f"Search results: {results}")
            json_results = [{"id": res["id"], "score": res["score"]} for res in results["matches"]]
            #input()
            return json_results
        except Exception as e:
            print(f"Failed to search embeddings: {e}")
            raise
