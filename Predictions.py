# Created by: Daniel Bemerguy 
# 04/01/2021 at 23:13
#Testing the model with an outside dataset
#Loading dataset
critics = pd.read_excel("output.xlsx", engine="openpyxl")
critics = pd.DataFrame(critics)
critics = critics[['movies',"critics"]]
critics = critics[critics['critics'].notnull()] #remove NaNs

#Function to remove stop words from movies dataset
def process_critic(critic):
    processed_critic = critic
    processed_critic = " ".join(word for word in processed_critic.split() if word not in stop_words) #remove stop words
    processed_critic = " ".join(Word(word).lemmatize() for word in processed_critic.split()) #lemmatize words
    return(processed_critic)


critics["processed_critics"] = critics["critics"].apply(lambda x:process_critic(x)) #apply function to all DataFrame