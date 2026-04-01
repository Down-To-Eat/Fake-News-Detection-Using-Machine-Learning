# **FAKE NEWS DETECTION USING MACHINE LEARNING**



### **Project Overview**



**In today’s digital world, social media platforms spread information very quickly. However, not all information is true. Many fake news articles can mislead people and create confusion.**



**This project aims to solve this problem by building a Machine Learning model that can automatically detect whether a news article is:**



* **Real News**
* **Fake News**



**The model analyzes the text of the news and predicts its authenticity.**



### **Problem Statement**



**Nowadays, fake news spreads quickly on the internet, and it is not easy for people to verify every news article manually.**



**So, the main goal of this project is:**



**To build a system that can automatically detect whether a news article is real or fake using machine learning.**



### **Dataset Used**



##### **Dataset Name :**



**ISOT Fake News Dataset**



##### **Source :**



**I downloaded this dataset from Kaggle.**



##### **Files Used :**



* **Fake.csv → Contains fake news articles**
* **True.csv → Contains real news articles**



##### **Dataset Features :**



**Each file contains:**



* **title → News headline**
* **text → Full news content**
* **subject → Category of the news**
* **date → Date when the news was published**



##### **Why I chose this dataset :**



* **It is clean and easy to use**
* **It is commonly used for fake news detection projects**
* **It has a large number of news articles**



### **Reducing Dataset Size (For GitHub Upload)**



**The original dataset files are large (50 mb \[True.csv] and 62 mb \[False.csv] respectively) and exceeds GitHub’s upload limit (25 mb).**

**So we need to reduce file size, so that we can keep only a portion of the dataset while being within the upload limit.**



##### **Run the following script : Predict.py**



###### **CODE :**



**import pandas as pd**



**fake = pd.read\_csv("Fake.csv")**

**true = pd.read\_csv("True.csv")**



**fake = fake.head(3000)**

**true = true.head(3000)**



**fake.to\_csv("Fake.csv", index=False)**

**true.to\_csv("True.csv", index=False)**



**print("Dataset reduced successfully!")**



###### **What this does:**



* **Keeps only the first 3000 rows**
* **Reduces file size below GitHub limit**
* **Maintains enough data for training**



### **Technologies Used**



##### **Programming Language:**



**Python**



##### **IDE:**



**VS Code**



##### **Libraries Used :**



* **pandas – for handling data**
* **numpy – for numerical operations**
* **scikit-learn – for machine learning model**
* **nltk – for text processing**
* **string**
* **pickle**



### **Machine Learning Approach**



### **1. Data Preprocessing**



**Before training the model, the text data needs to be cleaned. I performed the following steps:**



* **Converted text to lowercase**
* **Removed punctuation**
* **Removed stopwords (common words like "the", "is", etc.)**
* **Tokenization (splitting sentences into words)**



**This step helps the model understand the text better.**



##### **2. Feature Extraction**



**Machines cannot understand text directly, so we need to convert text into numbers.**



**For this, I used:**



* **TF-IDF (Term Frequency – Inverse Document Frequency)**



**This technique helps the model focus more on important words in the article.**



##### **3. Model Used**



**I used Logistic Regression for this project.**



**Reasons for choosing it:**



* **It is simple and effective**
* **Works well for text classification**
* **Easy to train and understand**



###### **Model Training :**



**The model is trained using the file: trainmodel.py**



###### **Where is the model trained ?**



* **The model is trained on my computer using Python.**
* **It uses the dataset files (Fake.csv and True.csv) stored in the project folder.**



###### **What happens during training ?**



**During training:**



* **The dataset is loaded**
* **Text data is cleaned**
* **TF-IDF converts text into numbers**
* **The model learns patterns between real and fake news**
* **Accuracy of the model is calculated**



###### **Output of training :**



**After training, two files are created:**



* **model.pkl → The trained machine learning model**
* **vectorizer.pkl → The TF-IDF vectorizer**



**These files are saved in the project folder and used later for prediction.**



### **Prediction System**



###### **Prediction is done using the file:**



**predict.py**



##### **How it works :**



* **The user enters a news article**
* **The text is cleaned**
* **It is converted into numerical format**
* **The model predicts whether the news is real or fake**



###### **Output:**



* **This is a Real News**
* **This is a Fake News**



### **How to Run the Project**



##### **Step 1: Install Requirements**



###### **RUN -**



**pip install -r requirements.txt**



**This will download all the libraries required for the project.**



##### **Step 2: Train the Model**



###### **RUN -**



**python trainmodel.py**



###### **This will :**



1. **Load the dataset (Fake.csv and True.csv) and combines them into one dataset with labels (fake = 0, real = 1).**
2. **It cleans and preprocesses the text by removing punctuation, converting to lowercase, and removing stopwords.**
3. **The text is converted into numerical form using TF-IDF, and the model (Logistic Regression) is trained on this data.**
4. **After training, it evaluates accuracy and saves the model as model.pkl and vectorizer.pkl for future predictions.**



##### **Step 3: Run Prediction**



##### **RUN -**



**python predict.py**



###### **This will :**



1. **Run the Python script, which loads the already trained model (model.pkl) and vectorizer (vectorizer.pkl).**
2. **Take user input (news text) and cleans it (removes punctuation, stopwords, etc.).**
3. **The cleaned text is converted into numbers using TF-IDF, so the model can understand it.**
4. **The model then analyzes the input and predicts whether the news is Real or Fake, and displays the result.**





### **Example**



##### **Input :**



**Breaking News: WASHINGTON (Reuters) - Alabama Secretary of State John Merrill said he will certify Democratic Senator-elect Doug Jones as winner on Thursday despite opponent Roy Moore’s challenge, in a phone call on CNN. Moore, a conservative who had faced allegations of groping teenage girls when he was in his 30s, filed a court challenge late on Wednesday to the outcome of a U.S. Senate election he unexpectedly lost.**



##### **Output :**



**This is a Real News**



### **Results**



* **Model Accuracy: Around 90–95%**
* **The model performs well in identifying fake news**
* **Prediction is fast and simple**



### **Challenges Faced**



**While doing this project, I faced some challenges:**



* **Handling a large dataset**
* **Cleaning messy text data**
* **Reducing Dataset Size to fit GitHub File Upload Limit (25 MB)**
* **Preventing overfitting**
* **Making sure the dataset was properly arranged**



**But solving these problems helped me learn more about machine learning.**





### **Future Improvements**



**In the future, this project can be improved by:**



* **Using Deep Learning models like LSTM or BERT**
* **Increasing Dataset Size to upgrade and update the model**
* **Creating a website or web app for this system**
* **Detecting news in real time**
* **Improving the accuracy of the model**



### **Learning Outcomes**



**From this project, I learned:**



* **Basics of Natural Language Processing (NLP)**
* **How to clean and process text data**
* **How machine learning models work**
* **How to train and test a model**
* **How AI can be used to solve real-world problems**



**This project was a great learning experience for me.**



### **Project Structure**



**Folder Name -->> fake-news-detection**



**Files :**



1. **Fake.csv**
2. **True.csv**
3. **requirements.txt**
4. **reducedataset.py**
5. **train\_model.py**
6. **model.pkl**
7. **vectorizer.pkl**
8. **predict.py**

