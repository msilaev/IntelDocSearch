import React from 'react';

interface Result {
    id: string;
    score: number;
    text?: string;  // Optional field for text snippet
    title?: string; // Optional field for title
}

interface ResultsDisplayProps {
    results: Result[];
}

const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ results }) => {
    return (
        <div>
            <h2>Search Results</h2>
            <ul>
                {results.map((result, index) => (
                    <li key={index}>
                        <strong>ID:</strong> {result.id}, <strong>Score:</strong> {result.score}
                        {result.title && <div><strong>Title:</strong> {result.title}</div>}
                        {result.text && <div><strong>Snippet:</strong> {result.text}</div>}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ResultsDisplay;