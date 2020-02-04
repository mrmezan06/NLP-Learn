# -*- coding: utf-8 -*-

import numpy as np
import re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files
# nltk.download('stopwords')

#importing datasets needs only root folder for loading data
# work only C drive on Windows
reviews = load_files('txt_sentoken')
# 0 --> neg and 1 -->pos because of indexing folder
X,y = reviews.data,reviews.target
# Storing as pickle files
with open('X.picle', 'wb') as f:
    pickle.dump(X,f)
with open('y.picle', 'wb') as f:
    pickle.dump(y,f)
    
# Unpickling the dataset it is first load the data more than 50 times faster
with open('X.picle','rb') as f:
    X = pickle.load(f)
with open('y.picle','rb') as f:
    y = pickle.load(f)

# Creating the corpus
corpus = []
for i in range(0, len(X)):
    review = re.sub(r'\W',' ',str(X[i]))
    review = review.lower()
    review = re.sub(r'\s+[a-z]\s+',' ',review)
    review = re.sub(r'^[a-z]\s+',' ',review)
    review = re.sub(r'\s+',' ',review)
    corpus.append(review)
    
# Create BOW Model
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features=2000,min_df=3,max_df=0.6,stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()

#Transform BOW model to TF-IDF Model

from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
X = transformer.fit_transform(X).toarray()

#Tfidf vectorizer for predicting value
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=2000,min_df=3,max_df=0.6,stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()


# Creating two dataset one training set and one test set
from sklearn.model_selection import train_test_split
text_train,text_test,sent_train,sent_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Fit the loginstic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(text_train,sent_train)

# Test model performance
sent_pred = classifier.predict(text_test)

# Visualization Computer vs Real 
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(sent_test, sent_pred)

#Accuracy
total = cm[0][0] + cm[1][1]
ac = total/4
print("Accuracy : ",ac)

# Saving Model as Pickle File
with open('classifier.pickle','wb') as f:
    pickle.dump(classifier,f)
    
#Pickling Vectorizer
with open('tfidfmodel.pickle','wb') as f:
    pickle.dump(vectorizer,f)   
    
# testing imported model and user input sentence test
with open('classifier.pickle','rb') as f:
    clf = pickle.load(f)
    
with open('tfidfmodel.pickle','rb') as f:
    tfidf = pickle.load(f)

sample = ["You are a nice person, have a good life"]
sample = tfidf.transform(sample).toarray()
print(clf.predict(sample))



