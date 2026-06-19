import json
import os
import joblib
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "intent_classifier.pkl")
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

_embedding_model = None
_svm_model = None

def train():
    data_path = os.path.join(BASE_DIR, "data", "tasks.json")
    print(f"Loading dataset from {data_path}...")
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [item["user_input"] for item in data]
    labels = [item["intent"] for item in data]

    print(f"Loading embedding model: {EMBEDDING_MODEL_NAME}...")
    model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    
    print("Encoding texts to embeddings...")
    embeddings = model.encode(texts)

    X_train, X_test, y_train, y_test = train_test_split(embeddings, labels, test_size=0.2, random_state=42)

    print("Training SVC classifier...")
    svm_model = SVC(kernel="linear", probability=True, random_state=42)
    svm_model.fit(X_train, y_train)

    predictions = svm_model.predict(X_test)
    
    print("\n--- Classification Report ---")
    print(classification_report(y_test, predictions))
    
    accuracy = np.mean(predictions == y_test)
    print(f"Model accuracy on test set: {accuracy:.4f}")

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    save_dict = {
        "svm": svm_model,
        "embedding_model_name": EMBEDDING_MODEL_NAME
    }
    joblib.dump(save_dict, MODEL_PATH)
    print(f"\nModel dict saved to {MODEL_PATH}")

def predict(text: str) -> str:
    """Loads the model and predicts the intent for a given text."""
    global _embedding_model, _svm_model
    
    if _embedding_model is None or _svm_model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Please train the model first.")
            
        saved_dict = joblib.load(MODEL_PATH)
        _svm_model = saved_dict["svm"]
        emb_model_name = saved_dict["embedding_model_name"]
        
        # Load SentenceTransformer
        _embedding_model = SentenceTransformer(emb_model_name)
    
    # Encode the input text
    embedding = _embedding_model.encode([text])
    
    # Return predicted intent
    prediction = _svm_model.predict(embedding)[0]
    return prediction

if __name__ == "__main__":
    train()
