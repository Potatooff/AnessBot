from nltk.corpus import stopwords;from string import punctuation
import functools


"""Remove punctuation"""
@functools.lru_cache(maxsize=None)
def clean_text(text:str) -> str:
    stop_words = set(stopwords.words('english'))
    text = [word for word in text.split() if word.lower() not in stop_words]
    text = " ".join(text); text = text.lower()
    text = text.translate(str.maketrans("", "", punctuation))
    return text
