import re

def summarize(text: str) -> str:
    """Summarizes text using a simple extractive approach."""
    words = text.split()
    if len(words) < 30:
        return text + "\n(Note: Text too short for summarization)"
    
    # Simple sentence splitting using regex
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    
    # Return first 2-3 sentences depending on availability
    summary_sentences = sentences[:3]
    return " ".join(summary_sentences)
