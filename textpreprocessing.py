import string
text="""
Natural Language Processing (NLP) is a fascinating field of Artificial Intelligence.
It helps computers understand, interpret, and generate human language.
"""
text=text.lower()
text=text.translate(str.maketrans('','',string.punctuation))
tokens=text.split()

print("cleaned&tokenized text:")
print(tokens)