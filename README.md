---
title: Agentic AI System
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

**Live Demo:** https://huggingface.co/spaces/ananthan7703/agentic-ai-system

# Agentic AI Workflow Automation System

The Agentic AI Workflow Automation System is an intelligent, intent-aware conversational agent designed to route user queries and automate various business workflows. By analyzing the user's text, it determines the underlying intent and executes the corresponding specialized tool to accomplish the task efficiently.

## Tech Stack

* **Python**
* **FastAPI**
* **Gradio**
* **SentenceTransformers**
* **SVM**
* **scikit-learn**
* **Docker**

## Project Structure

```text
agentic-ai-system/
├── agent/               # Agent orchestration and intent routing
├── api/                 # FastAPI backend application
├── data/                # Training datasets and storage
├── logs/                # System logs
├── models/              # Saved ML models (SVM, vectorizers)
├── tools/               # Intent-specific execution tools
├── ui/                  # Gradio frontend interface
├── docker-compose.yml   # Docker compose configuration
├── Dockerfile           # Docker image definition
├── requirements.txt     # Python dependencies
└── train.py             # Model training script
```

## How It Works

* The user sends a text query via the Gradio frontend interface.
* The system routes the query to the FastAPI backend, where it is vectorized using SentenceTransformers.
* An SVM classifier predicts the intent of the query based on the text embedding.
* The orchestrator selects and executes the specialized tool corresponding to the predicted intent, returning the result to the user.

## Supported Intents

* **Summarization:** Generates concise summaries from provided long-form text.
* **Sentiment Analysis:** Detects the sentiment (positive, negative, neutral) of the input text.
* **Email Drafting:** Automatically drafts professional emails based on brief instructions.
* **Keyword Extraction:** Identifies and extracts key terms from the given document.
* **FAQ Search:** Searches a database of frequently asked questions to provide relevant answers.
* **Note Generation:** Structures raw thoughts or bullet points into organized meeting notes.

## How to Run Locally

1. Clone the repository to your local machine.
2. Create a virtual environment and install the requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Train the intent classifier model:
   ```bash
   python train.py
   ```
4. Start the FastAPI backend server:
   ```bash
   uvicorn api.main:app --reload --port 8000
   ```
5. In a separate terminal, start the Gradio UI:
   ```bash
   python ui/app.py
   ```

## How to Run with Docker

1. Build the Docker images:
   ```bash
   docker-compose build
   ```
2. Start the services in detached mode:
   ```bash
   docker-compose up -d
   ```

## API Endpoints

| Method | Endpoint   | Description                                       |
|--------|------------|---------------------------------------------------|
| GET    | `/`        | Health check and API status verification          |
| POST   | `/chat`    | Submits a user query and returns the agent's response |
| GET    | `/history` | Retrieves the current session's conversation history  |
| POST   | `/clear`   | Clears the current session's memory and chat history  |

## Classifier Performance

The intent classifier operates with an accuracy of **85.42%**, utilizing a `SentenceTransformer` (`all-MiniLM-L6-v2`) for generating dense embeddings combined with a Support Vector Machine (`SVM`) for intent classification.

## Known Limitations

* The system occasionally experiences misclassification between the `summarize` and `note` generation intents due to semantic similarities in the training data.
