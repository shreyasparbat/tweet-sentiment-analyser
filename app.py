# Library imports
from flask import Flask
import re
from textblob import Textblob

app = Flask(__name__)


# GET: Sentiments for chart
@app.route('/getSentiments')
def get_sentiments():
    return 'Hello World!'


# GET: Frequency of top 30 words
@app.route('/getWordCounts')
def get_word_counts():
    return 0


# Return the sentiment of the tweet
def get_sentiment(tweet):
    # Clean tweet by removing special characters and hyperlinks
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    # Use Textblob to get and return sentiment
    analysis = Textblob(tweet)
    return analysis.sentiment.polarity * 100


if __name__ == '__main__':
    app.run()
