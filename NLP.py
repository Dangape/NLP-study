# Created by: Daniel Bemerguy 
# 31/12/2020 at 13:57
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
from textblob import Word,TextBlob
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import SVC
from sklearn import model_selection
import pickle

#NLP
#Download only at the first time you run the code
# nltk.download("stopwords")
# nltk.download("wordnet")
# nltk.download("movie_reviews")
stop_words = stopwords.words("english")

#Create dict with frequency of words in movie_reviews dataset
all_words = nltk.FreqDist(movie_reviews.words())

#Define feature vector containing first 4000 words excluding stop words
feature_vector = list(word for word in all_words if word not in stop_words)

#List of words of a review and the category of the review
document = [(movie_reviews.words(file_id),category) for file_id in movie_reviews.fileids() for category in movie_reviews.categories(file_id)]
document = pd.DataFrame(document)
document.columns = ["reviews","sentiment"]

def remove_stop_words(review):
    processed_critic = list(word for word in review if word not in stop_words)
    return  processed_critic

document["reviews"] = document["reviews"].apply(lambda x:remove_stop_words(x)) #apply function to all DataFrame


#Function to search for the words of the review in the feature_vector
def find_feature(word_list):
    feature = {}
    for x in feature_vector:
        feature[x] = x in word_list

    return(feature)

document = document.values.tolist()

feature_sets = [(find_feature(word_list),category) for (word_list,category) in document]

#Using a SVC model to predict the sentiment of a review
train_set,test_set = model_selection.train_test_split(feature_sets,test_size = 0.25)

model = SklearnClassifier(SVC(kernel = "linear"))
model.train(train_set)

accuracy = nltk.classify.accuracy(model, test_set)
print('SVC Accuracy : {}'.format(accuracy))

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

