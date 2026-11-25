from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

text = "She was reading a book about the history of space travel"

words = word_tokenize(text)
stop = stopwords.words("english")

result = []
for word in words:
    if word.lower() not in stop:
        result.append(word)

print("Words without stopwords:")
print(result)
