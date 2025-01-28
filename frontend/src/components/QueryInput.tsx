import React, { useState, ChangeEvent } from 'react';

interface QueryInputProps {
    onSearch: (query: string) => void;
}


const QueryInput: React.FC<QueryInputProps> = ({ onSearch }) => {
    const [query, setQuery] = useState<string>('');

    const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
        setQuery(event.target.value);
    };

    const handleSearch = () => {
        if (query.trim()) {
            onSearch(query);
            setQuery('');
        }
    };

    return (
        <div>
            <input type="text" value={query} onChange={handleInputChange} />
            <button onClick={handleSearch}>Search</button>
        </div>
    );
};

export default QueryInput;