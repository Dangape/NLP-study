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

#Function to remove stop words from movies dataset
def process_critic(critic):
    processed_critic = critic
    processed_critic = " ".join(word for word in processed_critic.split() if word not in stop_words) #remove stop words
    return(processed_critic)


critics["critics_processed"] = critics["critics"].apply(lambda x:process_critic(x)) #apply function to all DataFrame
critics["critics_processed"] = critics["critics_processed"].apply(lambda x:re.findall(r"[\w']+|[.,!?;]",x)) #apply function to all DataFrame to split words and punctuation

critics = critics["critics_processed"]
critics = critics.values.tolist()
print(critics[0])

feature_vector = pickle.load(open("feature_vector.pickle", "rb"))

# This is how the Naive Bayes classifier expects the input
def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words if word in useful_words])
    return my_dict


test_data = "It would be impossible to sum up all the stuff that sucks about this film, so I'll break it down into what I remember most strongly: a man in an ingeniously fake-looking polar bear costume (funnier than the 'bear' " \
            "from Hercules in New York); an extra with the most unnatural laugh you're ever likely to hear; an ex-dope addict martian with tics; kid actors who make sure every syllable of their lines are slowly and caaarreee-fulll-yyy prrooo-noun-ceeed; " \
            "a newspaper headline stating that Santa's been 'kidnaped', and a giant robot. Yes, you read that right. A giant robot."

words = word_tokenize(test_data)
words = create_word_features(words)
print(words)

#Loading saved model
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

print(loaded_model.labels())
print(loaded_model.classify(words))
pred = nltk.classify(loaded_model, words)
print(pred)