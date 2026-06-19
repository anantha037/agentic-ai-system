from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text: str) -> list:
    """Extracts top keywords using TF-IDF."""
    if not text.strip() or len(text.split()) < 3:
        return text.split()
        
    try:
        # Use simple TF-IDF
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([text])
        feature_names = vectorizer.get_feature_names_out()
        
        # Get scores
        scores = tfidf_matrix.toarray()[0]
        
        # Sort by score descending and get top 5
        word_scores = [(feature_names[i], float(scores[i])) for i in range(len(feature_names))]
        word_scores.sort(key=lambda x: x[1], reverse=True)
        
        top_keywords = [word for word, score in word_scores[:5]]
        return top_keywords
    except Exception as e:
        # Fallback if text is too simple/empty for TF-IDF
        return text.split()[:5]
