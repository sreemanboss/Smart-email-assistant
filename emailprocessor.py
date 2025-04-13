class EmailProcessor:
    def summarize_email(self, email_content):
        """
        Returns a basic summary (first 100 characters).
        In production, replace this with NLP-based summarization.
        """
        if not email_content.strip():
            return "No content to summarize."
        return f"Summary: {email_content[:100]}..."

    def suggest_action(self, email_content):
        """
        Suggest an action based on keywords in the email content.
        """
        content = email_content.lower()
        if "meeting" in content:
            return "Schedule a meeting"
        elif "invoice" in content:
            return "Review or pay the invoice"
        elif "deadline" in content:
            return "Check and update your calendar"
        else:
            return "Reply or mark as read"

    def generate_reply(self, email_content):
        """
        Generates a placeholder reply. Replace with AI-generated reply in future.
        """
        return "Thank you for your email. I'll get back to you soon."
