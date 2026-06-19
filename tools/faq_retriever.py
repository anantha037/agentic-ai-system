FAQ_DB = {
    "refund policy": "You can request a full refund within 30 days of your purchase. Please contact support to initiate the process.",
    "shipping": "Standard shipping takes 3-5 business days. Expedited shipping is available at checkout for an additional fee.",
    "password reset": "To reset your password, click on the 'Forgot Password' link on the login page and follow the instructions sent to your email.",
    "account deletion": "You can delete your account from the account settings page. Please note that this action is irreversible.",
    "payment methods": "We accept all major credit cards, PayPal, and Apple Pay.",
    "contact support": "You can reach our support team via email at support@example.com or by calling 1-800-123-4567.",
    "order tracking": "Once your order ships, you will receive a tracking link via email to monitor its delivery status.",
    "return policy": "Items can be returned in their original packaging within 14 days of delivery. Return shipping is free.",
    "subscription cancellation": "You can cancel your subscription at any time from your billing dashboard. You will retain access until the end of the billing cycle.",
    "technical support": "For technical issues, please submit a ticket through our helpdesk portal with details of the problem."
}

def retrieve_faq(query: str) -> str:
    """Retrieves an FAQ answer using keyword matching."""
    query_lower = query.lower()
    
    best_match = None
    max_overlap = 0
    
    for topic, answer in FAQ_DB.items():
        # Simple overlap count
        topic_words = set(topic.split())
        query_words = set(query_lower.split())
        
        overlap = len(topic_words.intersection(query_words))
        
        # Extra points if the exact topic phrase is in the query
        if topic in query_lower:
            overlap += 5
            
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = answer
            
    if best_match and max_overlap > 0:
        return best_match
    
    return "No matching FAQ found"
