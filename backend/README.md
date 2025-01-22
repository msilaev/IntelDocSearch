# Intelligent Document Search and Summarization Tool - Backend

## Overview
This backend application serves as the core of the Intelligent Document Search and Summarization Tool. It is built using FastAPI and provides APIs for document upload, search, and summarization.

## Project Structure
- **app/**: Contains the main application code.
  - **main.py**: Entry point for the FastAPI application.
  - **api/**: Defines the API routes.
  - **services/**: Contains the business logic for searching and summarizing documents.
  - **models/**: Defines the data models used in the application.
  - **utils/**: Utility functions for various tasks, including vector database interactions.

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
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

4. **Run the application**:
   ```
   uvicorn app.main:app --reload
   ```

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

