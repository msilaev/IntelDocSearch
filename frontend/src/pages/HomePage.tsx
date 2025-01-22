import React from 'react';
import FileUpload from '../components/FileUpload';
import QueryInput from '../components/QueryInput';
import ResultsDisplay from '../components/ResultsDisplay';

const HomePage: React.FC = () => {
    return (
        <div>
            <h1>Intelligent Document Search</h1>
            <FileUpload />
            <QueryInput />
            <ResultsDisplay />
        </div>
    );
};

export default HomePage;