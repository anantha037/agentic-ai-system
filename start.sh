#!/bin/bash
# Start FastAPI backend in the background
uvicorn api.main:app --host 0.0.0.0 --port 8000 &

# Wait for FastAPI to be ready
sleep 5

# Start Gradio UI in the foreground
python ui/app.py
