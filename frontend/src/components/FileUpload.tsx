import React from 'react';

interface FileUploadProps {
    onFileSelect: (file: File) => void;
}

const FileUpload: React.FC<FileUploadProps> = ({ onFileSelect }) => {
    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files.length > 0) {
            onFileSelect(event.target.files[0]);  // Immediately pass the file
        }
    };

    return (
        <div>
            <input type="file" accept=".pdf, .doc, .docx, .txt" onChange={handleFileChange} />
        </div>
    );
};

export default FileUpload;
