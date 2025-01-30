import React, { useState } from 'react';

interface QueryInputProps {
    onSearch: (query: string) => void;
}

const QueryInput: React.FC<QueryInputProps> = ({ onSearch }) => {  // Add the missing opening curly brace
    const [query, setQuery] = useState('');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        onSearch(query);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                placeholder="Enter search query"
            />
            <button type="submit">Search</button>
        </form>
    );
};

export default QueryInput;