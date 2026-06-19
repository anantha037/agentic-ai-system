import json
import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_and_evaluate():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data", "tasks.json")
    model_path = os.path.join(base_dir, "models", "intent_classifier.pkl")

    print(f"Loading dataset from {data_path}...")
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [item["user_input"] for item in data]
    labels = [item["intent"] for item in data]

    # 80/20 train/test split
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression())
    ])

    print("Training intent classifier pipeline...")
    pipeline.fit(X_train, y_train)

    # Evaluate the model
    predictions = pipeline.predict(X_test)
    
    print("\n--- Classification Report ---")
    print(classification_report(y_test, predictions))

    # Save the trained model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(pipeline, model_path)
    print(f"\nModel trained and saved to {model_path}")

if __name__ == "__main__":
    train_and_evaluate()
