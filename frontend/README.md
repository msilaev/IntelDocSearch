# Frontend README.md

# Intelligent Document Search and RAG Tool - Frontend

## Overview
This is the frontend component of the Intelligent Document Search and Summarization Tool. It provides a user interface for uploading documents, entering search queries, and displaying search results and summaries.

## Getting Started

### Prerequisites
- Node.js (version 14 or higher)
- npm (Node Package Manager)

### Installation
1. Clone the repository:
   ```
   git clone git@github.com:msilaev/IntelDocSearch.git
   ```
2. Navigate to the frontend directory:
   ```
   cd intelligent-doc-search/frontend
   ```
3. Install the dependencies:
   ```
   npm install
   ```
 
### Running the Application
To start the development server, run:
```
npm start
```
This will launch the application in your default web browser at `http://localhost:3000`.

### Building for Production
To create a production build, run:
```
npm run build
```
The production build will be generated in the `build` directory.

## Environment Variables
Create a `.env` file in the root of the frontend directory and add the following environment variables:
```
REACT_APP_BACKEND_URL=http://localhost:8000
```
This variable should point to the backend server URL.

## Project structure
```
frontend/
├── public/                 # Public assets
│   ├── index.html          # Main HTML file
│   └── ...                 # Other public assets
├── src/                    # Source files
│   ├── components/         # React components
│   │   ├── FileUpload.tsx  # Component for uploading files
│   │   ├── QueryInput.tsx        # Component for entering search queries
|   |   └── ResultsDisplay.tsx    # Component for displaying result 
|   |   
|   ├── pages/              # Page components
|   |   ├── HomePage.tsx    #  Home page component
│   ├── App.tsx             # Main App component
│   ├── index.js            # Entry point for the React application
│   └── index.tsx           # Entry point for the React application 
├── .env                    # Environment variables
├── package.json            # NPM package configuration
├── webpack.config.js       # Webpack module bundler
├── .babelrc                # Babel configuration
└── README.md               # Project README file
```

## API Endpoints
- **Upload Document**: `POST /upload/`
- **Search Query**: `POST /search/`
- **RAG Query**: `POST /rag/`

## RAG (Retrieval-Augmented Generation)
RAG is a technique that combines retrieval-based and generation-based methods to provide more accurate and contextually relevant responses. The RAG system retrieves relevant documents based on a query and then generates a response using the content of those documents. 

## Components
- **FileUpload**: Allows users to upload documents.
- **QueryInput**: Enables users to enter search queries.
- **ResultsDisplay**: Displays the search results and summaries.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.