def analyze_sentiment(text: str) -> dict:
    """Analyzes sentiment using a basic keyword scoring approach."""
    positive_words = {"good", "great", "excellent", "happy", "love", "best", "awesome", "fantastic", "positive"}
    negative_words = {"bad", "terrible", "awful", "hate", "worst", "poor", "sad", "negative", "horrible"}
    
    words = text.lower().split()
    score = 0.0
    
    for word in words:
        # Strip punctuation for cleaner matching
        clean_word = "".join(c for c in word if c.isalpha())
        if clean_word in positive_words:
            score += 1.0
        elif clean_word in negative_words:
            score -= 1.0
            
    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    else:
        label = "neutral"
        
    return {
        "label": label,
        "score": score
    }
