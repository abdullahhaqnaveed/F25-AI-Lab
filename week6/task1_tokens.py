import re

samples = ["AI, search!", "I can't log in.", "help@example.com",
           "CS4944 version 2.1", "", "یہ ایک مثال ہے"]

for text in samples:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print(repr(text), "whitespace:", ws, len(ws))
    print("word-like:", words, len(words))

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    for text in samples[:2]:
        print(text, model.tokenizer.tokenize(text))
except Exception as e:
    print("Model tokenizer not available:", e)
