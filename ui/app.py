import gradio as gr
from gradio import ChatMessage
import requests

API_BASE_URL = "http://127.0.0.1:8000"

def send_message(user_input, chat_history):
    if not user_input:
        return chat_history, "", "", ""
        
    try:
        response = requests.post(f"{API_BASE_URL}/chat", json={"message": user_input})
        response.raise_for_status()
        data = response.json()
        
        bot_response = data.get("response", data.get("message", "Success"))
        intent = data.get("intent", "none")
        tool_used = data.get("tool_used", data.get("tool", "none"))
        
        chat_history.append(ChatMessage(role="user", content=user_input))
        chat_history.append(ChatMessage(role="assistant", content=bot_response))
        
        return chat_history, intent, tool_used, ""
    except Exception as e:
        chat_history.append(ChatMessage(role="assistant", content=f"Error: {str(e)}"))
        return chat_history, "error", "none", ""

def clear_chat():
    try:
        requests.post(f"{API_BASE_URL}/clear")
    except Exception:
        pass
    return [], "", ""

with gr.Blocks() as demo:
    gr.Markdown("# Agentic AI Workflow Automation System")
    gr.Markdown("<small>Powered by Intent-Aware AI Agent</small>")
    
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(placeholder="Type your message here...", label="Input")
    
    with gr.Row():
        send_btn = gr.Button("Send")
        clear_btn = gr.Button("Clear")
        
    intent_output = gr.Textbox(label="Intent Detected", interactive=False)
    tool_output = gr.Textbox(label="Tool Used", interactive=False)
    
    send_btn.click(
        fn=send_message,
        inputs=[user_input, chatbot],
        outputs=[chatbot, intent_output, tool_output, user_input]
    )
    
    user_input.submit(
        fn=send_message,
        inputs=[user_input, chatbot],
        outputs=[chatbot, intent_output, tool_output, user_input]
    )
    
    clear_btn.click(
        fn=clear_chat,
        inputs=[],
        outputs=[chatbot, intent_output, tool_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
