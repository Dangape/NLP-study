# Created by: Daniel Bemerguy 
# 04/01/2021 at 23:13
import pandas as pd
import pickle
from nltk.corpus import stopwords
import re
import nltk
from nltk.tokenize import word_tokenize


#Testing the model with an outside dataset
#Loading dataset
critics = pd.read_excel("output.xlsx", engine="openpyxl")
critics = pd.DataFrame(critics)
critics = critics[['movies',"critics"]]
critics = critics[critics['critics'].notnull()] #remove NaNs
stop_words = stopwords.words("english")

feature_vector = pickle.load(open("feature_vector.pickle", "rb"))

# This is how the Naive Bayes classifier expects the input
def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words if word in useful_words])
    return my_dict

#Loading saved model
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

test_data = "It would be impossible to sum up all the stuff that sucks about this film, so I'll break it down into what I remember most strongly: a man in an ingeniously fake-looking polar bear costume (funnier than the 'bear' " \
            "from Hercules in New York); an extra with the most unnatural laugh you're ever likely to hear; an ex-dope addict martian with tics; kid actors who make sure every syllable of their lines are slowly and caaarreee-fulll-yyy prrooo-noun-ceeed; " \
            "a newspaper headline stating that Santa's been 'kidnaped', and a giant robot. Yes, you read that right. A giant robot."

words = word_tokenize(test_data)
words = create_word_features(words)
print(loaded_model.classify(words))

critics = pd.DataFrame(critics)
critics["critics_processed"] = critics["critics"].apply(lambda x:word_tokenize(x))
critics["critics_processed"] = critics["critics_processed"].apply(lambda x:create_word_features(x))
critics["sentiment"] = critics["critics_processed"].apply(lambda x:loaded_model.classify(x))

df = pd.DataFrame({"sentiment":[],
                   "year":[]})

neg = (len(critics[critics["sentiment"]=="neg"])/len(critics))*100
pos = (len(critics[critics["sentiment"]=="pos"])/len(critics))*100

print("{}% of the critics are negative".format(neg)+" and {}% are positive".format(pos))