import json
import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "tasks.json")
MODEL_PATH = os.path.join(BASE_DIR, "models", "intent_classifier.pkl")

def train():
    print(f"Loading dataset from {DATA_PATH}...")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Extract user_input and intent fields
    texts = [item["user_input"] for item in data]
    labels = [item["intent"] for item in data]
    
    # Create Pipeline: TfidfVectorizer + LogisticRegression
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression())
    ])
    
    print("Training intent classifier pipeline...")
    pipeline.fit(texts, labels)
    
    # Calculate and print accuracy score
    predictions = pipeline.predict(texts)
    accuracy = accuracy_score(labels, predictions)
    print(f"Training accuracy score: {accuracy:.4f}")
    
    # Save the trained model
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)

def predict(text: str) -> str:
    """Loads the model and predicts the intent for a given text."""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Please train the model first.")
        
    pipeline = joblib.load(MODEL_PATH)
    prediction = pipeline.predict([text])[0]
    return prediction

if __name__ == "__main__":
    train()
