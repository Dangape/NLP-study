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

#Loading dataset
critics = pd.read_excel("output.xlsx", engine="openpyxl")
critics = pd.DataFrame(critics)
critics = critics[['movies',"critics"]]
critics = critics[critics['critics'].notnull()] #remove NaNs

#NLP
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("movie_reviews")
stop_words = stopwords.words("english")

#Function to remove stop words and lemmatize
def process_critic(critic):
    processed_critic = critic
    processed_critic = " ".join(word for word in processed_critic.split() if word not in stop_words) #remove stop words
    processed_critic = " ".join(Word(word).lemmatize() for word in processed_critic.split()) #lemmatize words
    return(processed_critic)


critics["processed_critics"] = critics["critics"].apply(lambda x:process_critic(x)) #apply function to all DataFrame

#list with two sentiments in movie_reviews dataset (negative and positive)
sentiment = movie_reviews.categories()

#Create dict with frequency of words in movie_reviews dataset
all_words = nltk.FreqDist(movie_reviews.words())

#Define feature vector containing first 4000 words
feature_vector = list(all_words)[:4000]

#List of words of a review and the category of the review
document = [(movie_reviews.words(file_id),category) for file_id in movie_reviews.fileids() for category in movie_reviews.categories(file_id)]

#Function to search for the words of the review in the feature_vector
def find_feature(word_list):
    feature = {}
    for x in feature_vector:
        feature[x] = x in word_list

    return(feature)

feature_sets = [(find_feature(word_list),category) for (word_list,category) in document]