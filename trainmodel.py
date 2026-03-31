import pandas as pd
import numpy as np
import string
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")
fake["label"] = 0
true["label"] = 1

data = pd.concat([fake, true])
data = data.sample(frac=1).reset_index(drop=True)
data = data[["text", "label"]]

stopwords = set(stopwords.words("english"))

def cleantext(text):
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stopwords]
    return " ".join(words)

data["text"] = data["text"].apply(cleantext)
X = data["text"]
y = data["label"]
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
Xtrain = vectorizer.fit_transform(Xtrain)
Xtest = vectorizer.transform(Xtest)
model = LogisticRegression(max_iter=1000)
model.fit(Xtrain, ytrain)

ypred = model.predict(Xtest)
accuracy = accuracy_score(ytest, ypred)
print("Accuracy:", accuracy)
print(classification_report(ytest, ypred))

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
print("Model saved successfully!")