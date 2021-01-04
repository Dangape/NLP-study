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

#NLP
#Download only the first time you run the code
# nltk.download("stopwords")
# nltk.download("wordnet")
# nltk.download("movie_reviews")
stop_words = stopwords.words("english")



#Create dict with frequency of words in movie_reviews dataset
all_words = nltk.FreqDist(movie_reviews.words())

#Define feature vector containing first 4000 words excluding stop words
feature_vector = list(word for word in all_words if word not in stop_words)[:4000]

#List of words of a review and the category of the review
document = [(movie_reviews.words(file_id),category) for file_id in movie_reviews.fileids() for category in movie_reviews.categories(file_id)]
document = pd.DataFrame(document)
document.columns = ["reviews","sentiment"]

def remove_stop_words(review):
    processed_critic = list(word for word in review if word not in stop_words)
    return  processed_critic

document["processed_reviews"] = document["reviews"].apply(lambda x:remove_stop_words(x)) #apply function to all DataFrame


Function to search for the words of the review in the feature_vector
def find_feature(word_list):
    feature = {}
    for x in feature_vector:
        feature[x] = x in word_list

    return(feature)

feature_sets = [(find_feature(word_list),category) for (word_list,category) in document]

#Testing the model with an outside dataset
#Loading dataset
# critics = pd.read_excel("output.xlsx", engine="openpyxl")
# critics = pd.DataFrame(critics)
# critics = critics[['movies',"critics"]]
# critics = critics[critics['critics'].notnull()] #remove NaNs

#Function to remove stop words and lemmatize from movies dataset
# def process_critic(critic):
#     processed_critic = critic
#     processed_critic = " ".join(word for word in processed_critic.split() if word not in stop_words) #remove stop words
#     processed_critic = " ".join(Word(word).lemmatize() for word in processed_critic.split()) #lemmatize words
#     return(processed_critic)
#
#
# critics["processed_critics"] = critics["critics"].apply(lambda x:process_critic(x)) #apply function to all DataFrame