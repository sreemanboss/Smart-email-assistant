import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from transformers import pipeline

email_text = """
Dear team, I hope this email finds you well. I just wanted to follow up on the client presentation scheduled for next week.
Please make sure your slides are ready by Friday so we can do a dry run on Monday. Also, remember to update the Q2 financials in the report.
Let me know if you need anything from my side. Thanks, and great job on the last sprint review!
"""

# ---------- Extractive Summary (Sumy LexRank) ----------
def extractive_summary(email_text):
    parser = PlaintextParser.from_string(email_text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    extractive_summary = summarizer(parser.document, sentences_count=2)
    return " ".join([str(sentence) for sentence in extractive_summary])

# ---------- Abstractive Summary (HuggingFace API) ----------
def abstractive_summary(email_text):
    API_TOKEN = "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"  # Replace with your Hugging Face token
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    
    response = requests.post(API_URL, headers=headers, json={"inputs": email_text})
    summary = response.json()[0]['summary_text']
    return summary

# ---------- Dual Summarization Function ----------
def summarize_email(email_text, method="both"):
    if method == "extractive":
        return extractive_summary(email_text)
    elif method == "abstractive":
        return abstractive_summary(email_text)
    else:
        return extractive_summary(email_text), abstractive_summary(email_text)

# Example Usage:
method = "both"  # Try 'extractive', 'abstractive', or 'both'
extractive, abstractive = summarize_email(email_text, method)

print("✂️ Extractive Summary:")
print(extractive)

print("\n🧠 Abstractive Summary:")
print(abstractive)
