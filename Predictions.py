# Created by: Daniel Bemerguy 
# 04/01/2021 at 23:13
import pandas as pd
import pickle
from textblob import Word,TextBlob
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
import re


#Testing the model with an outside dataset
#Loading dataset
critics = pd.read_excel("output.xlsx", engine="openpyxl")
critics = pd.DataFrame(critics)
critics = critics[['movies',"critics"]]
critics = critics[critics['critics'].notnull()] #remove NaNs
stop_words = stopwords.words("english")

#Function to remove stop words from movies dataset
def process_critic(critic):
    processed_critic = critic
    processed_critic = " ".join(word for word in processed_critic.split() if word not in stop_words) #remove stop words
    return(processed_critic)


critics["critics_processed"] = critics["critics"].apply(lambda x:process_critic(x)) #apply function to all DataFrame
critics["critics_processed"] = critics["critics_processed"].apply(lambda x:re.findall(r"[\w']+|[.,!?;]",x)) #apply function to all DataFrame to split words and punctuation

critics = critics["critics_processed"]
critics = critics.values.tolist()
print(critics[0:2])

#Loading saved model
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
#result = loaded_model.score(X_test, Y_test)


# #Create dict with frequency of words in movie_reviews dataset
# all_words = nltk.FreqDist(movie_reviews.words())
#
# #Define feature vector containing first 4000 words excluding stop words
# feature_vector = list(word for word in all_words if word not in stop_words)
#
# feature_sets = [(find_feature(word_list),category) for (word_list,category) in document]