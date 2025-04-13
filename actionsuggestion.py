from transformers import pipeline

# Load the zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define possible action labels
candidate_labels = [
    "Add to Calendar",
    "Reply to Email",
    "Ignore",
    "Forward to someone",
    "Mark as Done",
    "Read later",
    "Request more info",
    "Send a file",
    "Acknowledge",
    "No action needed"
]

def suggest_actions(subject, body):
    text = subject + " " + body
    result = classifier(text, candidate_labels, multi_label=True)
    
    # Filter only high-confidence suggestions (score > 0.4)
    suggestions = [
        f"{label} ({round(score * 100)}%)"
        for label, score in zip(result['labels'], result['scores'])
        if score > 0.4
    ]
    
    return suggestions

# Example email
subject = "Follow up on meeting and file request"
body = "Hi, please send me the presentation and confirm the meeting time."

# Run the action suggestion
actions = suggest_actions(subject, body)
print("Suggested Actions:")
for action in actions:
    print("✅", action)
