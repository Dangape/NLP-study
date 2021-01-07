# NLP-study
This code was done exclusively with the porpose to study natural language processing and amchine learning.

The critics.py file does the web scrapping and fetch the top critics from the rotten tomatoes website
I used a movie metadata to get names of movies from 1992 to 2017. With these names I created an algorithm to fetch their top critics from rotten tomatoes.

The NLP.py creates functions to process the critics and use a NaiveBayes machine learning model to training the classifier.
The training data used was the movie_reviews dataset from the nltk package from python
The accuracy of the model was 78%, which is not high.

Finally, the Predictions.py file uses the model created to predict the sentiment of a critic fetched from rotten tomatoes.
