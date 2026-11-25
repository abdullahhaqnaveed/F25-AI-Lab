from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk

nltk.download("wordnet")

words = [("flies", "v"), ("walked", "v"), ("children", "n")]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

for word, tag in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word, pos=tag)
    print(word, "Stem:", stem, "Lemma:", lemma)
