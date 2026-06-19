import logging
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

from agent.memory import ConversationMemory
from agent import pipeline

# Setup Logging
logger = logging.getLogger("agent_api")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Console Handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# File Handler
file_handler = logging.FileHandler("logs/agent.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Global memory instance
memory = ConversationMemory()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Agent API started")
    yield
    logger.info("Agent API shutting down")

app = FastAPI(lifespan=lifespan)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": "Agentic AI System is running", "status": "ok"}

@app.post("/chat")
async def chat(request: ChatRequest, req: Request):
    logger.info(f"Received request: {req.method} {req.url.path} - message: {request.message}")
    try:
        result = pipeline.run(request.message, memory)
        logger.info(f"Response: intent detected={result['intent']}, tool used={result['tool_used']}")
        return result
    except Exception as e:
        logger.exception("An error occurred during pipeline execution")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def get_history():
    return {"history": memory.get_history()}

@app.post("/clear")
async def clear_history():
    memory.clear()
    return {"message": "Conversation history cleared"}
