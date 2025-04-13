from transformers import pipeline

# Load the text generation model
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_reply(subject, body):
    prompt = f"""Generate a professional and short email reply to the following message:
    
    Subject: {subject}
    Message: {body}
    
    Reply:"""

    response = generator(prompt, max_length=100, do_sample=True, temperature=0.7)
    return response[0]['generated_text']

# Example usage
subject = "Can you confirm the meeting at 3 PM?"
body = "Hi, just checking if we’re still on for the meeting today at 3 PM. Let me know."

reply = generate_reply(subject, body)
print("📝 Suggested Reply:\n", reply)
