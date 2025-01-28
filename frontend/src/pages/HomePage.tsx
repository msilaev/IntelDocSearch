import React, { useState } from 'react';
import FileUpload from '../components/FileUpload';
import QueryInput from '../components/QueryInput';
import ResultsDisplay from '../components/ResultsDisplay';

const HomePage: React.FC = () => {
    const [results, setResults] = useState<string[]>([]);

    const handleFileUpload = (file: File) => {
        console.log('File uploaded:', file);
        // Handle file upload logic here
    };

    const handleSearch = (query: string) => {
        console.log('Search query:', query);
        // Handle search logic here and update results
        setResults([`Result for "${query}"`]);
    };

    return (
        <div>
            <h1>Intelligent Document Search</h1>
            <FileUpload onFileUpload={handleFileUpload} />
            <QueryInput onSearch={handleSearch} />
            <ResultsDisplay results={results} />
        </div>
    );
};

export default HomePage;