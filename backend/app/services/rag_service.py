import os
import sys
import openai
from dotenv import load_dotenv
from app.services.embedding_service import EmbeddingService

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

load_dotenv()
openai.api_key = os.getenv("OPEN_AI_KEY")

class RAGService:
    def __init__(self, embedding_service: EmbeddingService):
        self.embedding_service = embedding_service
        openai.api_key = os.getenv("OPEN_AI_KEY")

    def retrieve_document_text(self, doc_id: str) -> str:
        return self.embedding_service.get_document_text(doc_id)

    def retrieve_and_generate(self, query: str, top_k: int = 5) -> str:
        # Retrieve relevant documents
        results = self.embedding_service.search_embeddings(query, top_k=top_k)
        print(results)
        
        # Retrieve the text content of the documents
        retrieved_texts = [self.retrieve_document_text(result['id']) for result in results]
        print(retrieved_texts)

        # Combine retrieved texts
        combined_text = " ".join(retrieved_texts)
        print(combined_text)

        # Generate response based on combined text and user query using OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant."},
                {"role": "user", "content": f"Based on the following documents, answer the question: {query}\n\n{combined_text}"}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()