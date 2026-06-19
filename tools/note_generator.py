import re
from datetime import datetime

def generate_note(text: str) -> str:
    """Generates a formatted note from text."""
    # Simple sentence splitting
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    note = f"### Meeting Notes\n**Date:** {date_str}\n\n**Key Points:**\n"
    
    for sentence in sentences:
        if sentence.strip():
            note += f"- {sentence.strip()}\n"
            
    return note
