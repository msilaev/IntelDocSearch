class Document:
    def __init__(self, title: str, content: str, metadata: dict = None):
        self.title = title
        self.content = content
        self.metadata = metadata if metadata is not None else {}

    def __repr__(self):
        return f"Document(title={self.title}, content_length={len(self.content)}, metadata={self.metadata})"