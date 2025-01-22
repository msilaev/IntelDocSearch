import React, { useState } from 'react';

const QueryInput = ({ onSearch }) => {
    const [query, setQuery] = useState('');

    const handleInputChange = (event) => {
        setQuery(event.target.value);
    };

    const handleSearch = () => {
        if (query.trim()) {
            onSearch(query);
            setQuery('');
        }
    };

    return (
        <div className="query-input">
            <input
                type="text"
                value={query}
                onChange={handleInputChange}
                placeholder="Enter your search query..."
            />
            <button onClick={handleSearch}>Search</button>
        </div>
    );
};

export default QueryInput;