class ConversationMemory:
    def __init__(self):
        self._history = []
        
    def add(self, role: str, content: str):
        if role not in ("user", "agent"):
            raise ValueError("Role must be 'user' or 'agent'")
        self._history.append({"role": role, "content": content})
        
    def get_history(self) -> list:
        return self._history
        
    def get_context_string(self) -> str:
        # Last 5 exchanges (up to 10 messages)
        recent = self._history[-10:]
        context_lines = []
        for msg in recent:
            context_lines.append(f"{msg['role'].capitalize()}: {msg['content']}")
        return "\n".join(context_lines)
        
    def clear(self):
        self._history.clear()
