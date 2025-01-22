from transformers import pipeline

class SummarizationService:
    def __init__(self):
        self.summarizer = pipeline("summarization")

    def summarize_text(self, text: str, max_length: int = 130, min_length: int = 30, do_sample: bool = False) -> str:
        summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
        return summary[0]['summary_text']

    def summarize_sections(self, sections: list) -> dict:
        summaries = {}
        for section in sections:
            title = section.get('title', 'Untitled')
            content = section.get('content', '')
            summaries[title] = self.summarize_text(content)
        return summaries