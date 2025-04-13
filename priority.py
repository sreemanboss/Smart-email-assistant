def detect_priority(subject, body):
    text = (subject + " " + body).lower()
    high_priority_keywords = ['urgent', 'asap', 'immediately', 'important', 'deadline', 'critical']
    low_priority_keywords = ['later', 'no rush', 'whenever', 'fyi', 'optional']

    if any(word in text for word in high_priority_keywords):
        return "High Priority"
    elif any(word in text for word in low_priority_keywords):
        return "Low Priority"
    else:
        return "Normal Priority"

# Example
subject = "Project Deadline Approaching"
body = "Please submit the final report by tomorrow. It's urgent."

print(detect_priority(subject, body))  # Output: High Priority
