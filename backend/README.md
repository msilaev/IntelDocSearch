# Intelligent Document Search and RAG Tool - Backend

## Overview
This backend application serves as the core of the Intelligent Document Search and RAG Tool. It is built using FastAPI and provides APIs for document upload, search, and retrieval augmented generation tool.

## Project Structure
```
backend/ 
├── app/                    # Main application code 
│ ├── main.py               # Entry point for the FastAPI application 
│ ├── api/                  # API routes 
│ │   └── routes.py         # Defines the API routes 
| |
│ ├── services/             # Business logic for searching and summarizing documents 
│ │   ├── embedding_service.py     # Service for handling embeddings 
│ │   ├── rag_service.py           # Service for retrieval-augmented generation 
│ │   ├── search_service.py        # Service for searching documents 
│ │   └── summarization_service.py # Service for summarizing documents 
| |
│ ├── models/                      # Data models used in the application 
│ │   └── document_model.py        # Model for document data 
| |
│ └── utils/                  # Utility functions 
│    └── vector_db.py         # Utility functions for vector database interactions 
| 
├── .env                      # Environment variables 
├── requirements.txt          # Python dependencies 
├── README.md                 # Project README file 
└── tests/                    # Test cases 
   ├── test_api.py            # Test cases for API routes 
   └── test_services.py       # Test cases for services
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone git@github.com:msilaev/IntelDocSearch.git
   cd intelligent-doc-search/backend
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Environment variables**
   Create a `.env` file in the root of the backend directory and add the necessary environment variables: `OPENAI_API_KEY=your_openai_api_key`,  `PINECONE_API_KEY=your_pinecone_api_key`

5. **Run the application**:
   ```
   uvicorn app.main:app --reload
   ```

## API Endpoints
- **Upload Document**: `POST /upload/`
- **Search Query**: `POST /search/`
- **RAG Query**: `POST /rag/`

## Databases
The backend application uses two types of databases:

### Vector Database (Pinecone)
 Pinecone is used as the vector database to store and query document embeddings. Embeddings are numerical representations of the documents that capture their semantic meaning. Pinecone provides efficient similarity search capabilities, allowing the application to quickly retrieve relevant documents based on query embeddings.

- **Storing Embeddings:** Document embeddings are stored in Pinecone using the store_embeddings method in the EmbeddingService class.

- **Querying Embeddings:** The search_embeddings method in the EmbeddingService class is used to query Pinecone for similar embeddings based on a query.

### SQLite Database
SQLite is used to store the actual text content of the documents. This allows the application to retrieve the full text of documents based on their IDs.

- **Storing Text:** Document texts are stored in the SQLite database using the store_embeddings method in the EmbeddingService class.
Retrieving Text: The get_document_text method in the EmbeddingService class is used to retrieve the text content of documents from the SQLite database.

- **Retrieving Text:** The get_document_text method in the EmbeddingService class is used to retrieve the text content of documents from the SQLite database.


## Usage
- The backend exposes several API endpoints for document upload, search, and summarization. Refer to the API documentation in `app/api/routes.py` for detailed information on available endpoints and their usage.

## Docker
To build and run the application using Docker, use the following commands:
1. **Build the Docker image**:
   ```
   docker build -t intelligent-doc-search-backend .
   ```

2. **Run the Docker container**:
   ```
   docker run -p 8000:8000 intelligent-doc-search-backend
   ```