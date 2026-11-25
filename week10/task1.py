from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")

text = "The weather is pleasant today. We should go for a walk!"

sentences = sent_tokenize(text)
print("Sentences:")
print(sentences)

words = word_tokenize(text)
print("Words:")
print(words)
