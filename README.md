# Predict-Language

I built this KNN model to predict a document's language using cosine similarity on its trigram frequency. I then built a simple interface using tkinter to easily upload a document and predict its language.

## Development
I consider this the very first machine learning project I ever did, and one of the earlier python projects so I didn't yet use common practices. My code wasn't very pythonic but regardless, I built a functioning model and interface that is worth sharing.

In predict_lang.py you can see the way I do the clustering. To start off I use a file named `languages.txt`. This file contains, essentially, the centers of the clusters for each language. I created this file, by going collecting a bunch of text data on a given language, calculating the trigram frequency and normalizing it. I found out that trigram frequency are very unique to each language so this is how I chose to embed the text. After I have those embeddings, whenever the model gets a new body of text, it will first embed the input text in the same way by collecting trigram frequency and normalizing it. Then, it will use cosine similarity to determine how close this input text is to the language embeddings. The dashboard will then display the top 3 highest languages.

The reason I chose cosine similarity instead of another distance function is mainly due to the high dimensionality of the embeddings, 27^3. For that reason, cosine similarity would have been the most accurate distance metric.

## Usage
Download the repo from github and run `main.py`. Do not change the directory structure.
That should open up a new window with instructions on how to use the application. Upload a document of your choice and the model will predict it is one of 7 languages: Croatian, Dutch, English, French, German, Spanish, Romanian. It will display the top 3 most likely languages.
