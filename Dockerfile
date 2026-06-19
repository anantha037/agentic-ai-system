FROM python:3.10-slim

WORKDIR /app

# Copy requirements first to leverage Docker layer caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Create necessary directories
RUN mkdir -p logs models

# Run the training script so the model is baked into the image
RUN python train.py

# Expose the API port
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
