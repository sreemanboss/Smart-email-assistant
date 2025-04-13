import nltk
import os

# Add local nltk data path
nltk_path = os.path.abspath("venv/nltk_data")
nltk.data.path.append(nltk_path)

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "Final check — hopefully no more errors now!"

tokens = word_tokenize(text)
tagged = pos_tag(tokens)

print("Tagged Output:")
for word, tag in tagged:
    print(f"{word} --> {tag}")
