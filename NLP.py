# Created by: Daniel Bemerguy 
# 31/12/2020 at 13:57
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
from textblob import Word,TextBlob

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

print(movie_reviews.categories())