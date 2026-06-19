import json
from agent.memory import ConversationMemory
from agent import classifier
from tools.summarizer import summarize
from tools.sentiment import analyze_sentiment
from tools.email_drafter import draft_email
from tools.keyword_extractor import extract_keywords
from tools.faq_retriever import retrieve_faq
from tools.note_generator import generate_note

def run(user_input: str, memory: ConversationMemory) -> dict:
    # STEP 1: Add user_input to memory as role "user"
    memory.add("user", user_input)
    
    # STEP 2: Call classifier.predict(user_input) to get intent
    intent = classifier.predict(user_input)
    
    # STEP 3: Strip the tool-specific prefix from user_input
    if ":" in user_input:
        clean_input = user_input.split(":", 1)[1].strip()
    else:
        clean_input = user_input.strip()
        
    # STEP 4: Route to the correct tool based on intent
    tool_used = ""
    response = ""
    
    if intent == "summarize":
        tool_used = "summarizer"
        response = summarize(clean_input)
    elif intent == "sentiment":
        tool_used = "sentiment"
        # Convert dict to string
        result_dict = analyze_sentiment(clean_input)
        response = json.dumps(result_dict)
    elif intent == "email":
        tool_used = "email_drafter"
        response = draft_email(clean_input)
    elif intent == "keyword":
        tool_used = "keyword_extractor"
        # Convert list to string
        result_list = extract_keywords(clean_input)
        response = ", ".join(result_list)
    elif intent == "faq":
        tool_used = "faq_retriever"
        response = retrieve_faq(clean_input)
    elif intent == "note":
        tool_used = "note_generator"
        response = generate_note(clean_input)
    else:
        tool_used = "none"
        response = "I am not sure how to handle that request."
        
    # STEP 5: Add the tool result to memory as role "agent"
    memory.add("agent", response)
    
    # STEP 6: Return a dict
    return {
        "intent": intent,
        "tool_used": tool_used,
        "response": response,
        "history": memory.get_history()
    }
