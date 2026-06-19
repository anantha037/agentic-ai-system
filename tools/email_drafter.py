def draft_email(context: str) -> str:
    """Drafts an email based on context."""
    words = context.split()
    
    # Extract subject hint (first 5 words)
    subject_hint = " ".join(words[:5]) + "..." if len(words) > 5 else context
    
    email_template = f"""Subject: Regarding {subject_hint}

Dear [Recipient Name],

I hope this email finds you well. I am writing to you regarding the following matter:

{context}

Please let me know if you need any further information or if we can schedule a quick call to discuss this in more detail.

Best regards,

[Your Name]
[Your Title/Company]
"""
    return email_template
