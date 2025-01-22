import React from 'react';

interface Result {
    title: string;
    summary: string;
    metadata: Record<string, any>;
}

interface ResultsDisplayProps {
    results: Result[];
}

const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ results }) => {
    return (
        <div className="results-display">
            {results.length === 0 ? (
                <p>No results found.</p>
            ) : (
                results.map((result, index) => (
                    <div key={index} className="result-item">
                        <h3>{result.title}</h3>
                        <p>{result.summary}</p>
                        <pre>{JSON.stringify(result.metadata, null, 2)}</pre>
                    </div>
                ))
            )}
        </div>
    );
};

export default ResultsDisplay;