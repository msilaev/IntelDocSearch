from dotenv import load_dotenv
import os
import numpy as np
import sqlite3
from sentence_transformers import SentenceTransformer
import pinecone
from pinecone import ServerlessSpec

load_dotenv()
pinecone_key = os.getenv("PINECONE_API_KEY")

class EmbeddingService:

    def __init__(self, model_name: str = 'all-MiniLM-L6-v2', db_path: str = 'documents.db'):
        self.model = SentenceTransformer(model_name)
        self.pc = pinecone.Pinecone(api_key=pinecone_key)
        
        # Create the index if it doesn't exist
        if 'document-embeddings' not in self.pc.list_indexes():
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
        print(text)
        print(f"Generated embeddings: {embeddings[:5]}...")  # Print first 5 values for debugging
        return embeddings
        
    def store_embeddings(self, doc_id: str, embeddings: np.ndarray, text: str):
        try:
            print(f"Storing embeddings for document ID: {doc_id}")
            embeddings_list = embeddings.astype(np.float32).flatten().tolist()

            # Ensure correct format for upsert
            self.index.upsert(vectors=[(doc_id, embeddings_list)])

            # Store document text in the database
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO documents (doc_id, text) VALUES (?, ?)", (doc_id, text))
            conn.commit()
            conn.close()

            print("Embeddings and document text stored successfully")
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
            results = self.index.query(vector=query_embedding.tolist(), top_k=top_k)
            json_results = [{"id": res["id"], "score": res["score"]} for res in results["matches"]]
            return json_results
        except Exception as e:
            print(f"Failed to search embeddings: {e}")
            raise