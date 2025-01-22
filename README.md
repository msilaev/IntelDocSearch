# Intelligent Document Search and Summarization Tool

## Overview
The Intelligent Document Search and Summarization Tool is an AI-powered application designed to help users efficiently search and summarize content from various document formats, including PDFs, Word files, and plain text. By leveraging advanced language models and semantic search techniques, this tool enables users to extract insights quickly and effectively.

## Features
- **AI-Driven Search**: Utilize large language models (LLMs) to interpret natural language queries and retrieve relevant document sections.
- **Context-Aware Summarization**: Generate concise summaries of highlighted sections, providing users with quick insights.
- **Interactive User Interface**: A user-friendly frontend built with React, allowing for document uploads and real-time query responses.
- **Semantic Search**: Implement a vector database for enhanced search accuracy and contextual relevance.

## Project Structure
The project is organized into three main directories:
- **backend**: Contains the FastAPI application, including API routes, services for search and summarization, and utility functions for database interactions.
- **frontend**: Contains the React application, including components for file upload, query input, and results display.
- **docs**: Documentation detailing the architecture, AI pipelines, database integration, and performance metrics.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Node.js and npm
- Docker (optional, for containerization)

### Installation

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd intelligent-doc-search
   ```

2. **Backend Setup**:
   - Navigate to the `backend` directory:
     ```
     cd backend
     ```
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. **Frontend Setup**:
   - Navigate to the `frontend` directory:
     ```
     cd frontend
     ```
   - Install the required Node packages:
     ```
     npm install
     ```

### Running the Application

1. **Start the Backend**:
   - In the `backend` directory, run:
     ```
     uvicorn app.main:app --reload
     ```

2. **Start the Frontend**:
   - In the `frontend` directory, run:
     ```
     npm start
     ```

3. **Access the Application**:
   - Open your web browser and navigate to `http://localhost:3000` to access the frontend.

## Performance Metrics
The application tracks various performance metrics, including:
- Precision and recall of search queries
- Latency and response quality of LLMs

## Extensions
Future enhancements may include:
- Voice-to-text capabilities for spoken queries
- Support for multi-language document processing
- A feedback loop to improve model performance based on user interactions

## License
This project is licensed under the MIT License. See the LICENSE file for more details.