import React, { useState } from 'react';
import axios from 'axios';
import FileUpload from '../components/FileUpload';
import QueryInput from '../components/QueryInput';
import ResultsDisplay from '../components/ResultsDisplay';

interface Result {
    id: string;
    score: number;
}
const HomePage: React.FC = () => {
    
    const [results, setResults] = useState<Result[]>([]);
    const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';
    const [ragResponse, setRagResponse] = useState<string>('');

    // Store the selected file
    const [file, setFile] = useState<File | null>(null);

    // Function to set file when selected
    const handleFileSelect = (selectedFile: File) => {
        setFile(selectedFile);
    };

    // Upload file to backend
    const handleUpload = async () => {
        if (!file) {
            alert("Please select a file first!");
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post(`${backendUrl}/upload/`, formData, {
                headers: { 'Content-Type': 'multipart/form-data' },
            });
            console.log("Response:", response.data);
            alert("File uploaded successfully!");
            setFile(null);  // Reset file after upload
        } catch (error) {
            console.error("Error uploading file:", error);
            alert("File upload failed!");
        }
    };

    // Handle search query
    const handleSearch = async (query: string, top_k: number = 5) => {
        try {
            const response = await axios.post(`${backendUrl}/search/`, { query, top_k });
            setResults(response.data.results);
        } catch (error) {
            console.error("Error searching:", error);
        }
    };

    // Handle RAG query
    const handleRAG = async (query: string, top_k: number = 5) => {
        try {
            const response = await axios.post(`${backendUrl}/rag/`, { query, top_k });
            setRagResponse(response.data.response);
        } catch (error) {
            console.error("Error in RAG:", error);
        }
    };

    return (
        <div>
            <h1>Intelligent Document Search</h1>
            <FileUpload onFileSelect={handleFileSelect} />
            <button onClick={handleUpload} disabled={!file}>
                Upload File
            </button>
            <QueryInput onSearch={handleSearch} />
            <ResultsDisplay results={results} />
            <h2>RAG Query</h2>
            <QueryInput onSearch={handleRAG} />
            {ragResponse && (
                <div>
                    <h3>RAG Response</h3>
                    <p>{ragResponse}</p>
                </div>
            )}
        </div>
    );
};

export default HomePage;
