import React from 'react';

interface ResultsDisplayProps {
    results: string[];
}

const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ results }) => {
    return (
        <div>
            <h2>Search Results</h2>
            <ul>
                {results.map((result, index) => (
                    <li key={index}>{result}</li>
                ))}
            </ul>
        </div>
    );
};

export default ResultsDisplay;