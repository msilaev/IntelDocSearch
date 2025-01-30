import React from 'react';

interface Result {
    id: string;
    score: number;
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
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ResultsDisplay;