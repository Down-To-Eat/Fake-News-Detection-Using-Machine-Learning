import pickle
import string
import nltk
from nltk.corpus import stopwords

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

s = set(stopwords.words("english"))

with open("model.pkl", "rb") as mfile:
    model = pickle.load(mfile)
with open("vectorizer.pkl", "rb") as vfile:
    vectorizer = pickle.load(vfile)

def cleantext(text):
    text = text.lower()
    text = "".join(char for char in text if char not in string.punctuation)
    words = text.split()
    filteredwords = []
    for word in words:
        if word not in s:
            filteredwords.append(word)
    return " ".join(filteredwords)

def predictnews(text):
    processedtext = cleantext(text)
    vector = vectorizer.transform([processedtext])
    prediction = model.predict(vector)[0]
    if prediction == 0:
        return "This is Fake News"
    else:
        return "This is Real News"

def main():
    print("Fake News Detection")
    print("-" * 25)
    newstext = input("Enter news text: ").strip()
    if not newstext:
        print("No input provided.")
        return
    result = predictnews(newstext)
    print("\nResult:", result)

if __name__ == "__main__":
    main()