# NLP-study
This code was done exclusively with the purpose to study natural language processing and machine learning.

The critics.py file does the web scrapping and fetches the top critics from the rotten tomatoes website
I used a movie metadata dataset from Kaggle to get names of movies from 1992 to 2017. With these names, I created an algorithm to fetch their top critics from rotten tomatoes.

The NLP.py creates functions to process the critics and use a NaiveBayes machine learning model to training the classifier.
The training data used was the movie_reviews dataset from the nltk package from python
The accuracy of the model was 78%, which is not high.

Finally, the Predictions.py file uses the model created to predict the sentiment of a critic fetched from rotten tomatoes.

I hope this codes help anyone who is a begginer in machine learning and NLP. Furthermore, I am not a computer scientist, hence, do not expect high quality and good practices on my coding.

Furthermore, how this code can be improved?

1. Using another machine learning model

2. Incorporate entity recognition and disambiguation

3. Use a larger dataset
