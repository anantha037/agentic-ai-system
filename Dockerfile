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

# Expose the Hugging Face Spaces default port
EXPOSE 7860

COPY start.sh .
RUN chmod +x start.sh

# Start both services using the script
CMD ["bash", "start.sh"]
