# Preprocessing
import pandas as pd
import re
from html import unescape

data = 'ai_model\preprocessing\SentimentTrain.csv'
df = pd.read_csv(data)

def emojis2Text(tweet):
    emojis = {
        "happy": ":\)",
        "cheerful": ":D",
        "sad": ":\("
        }
    
    for k in emojis:
        tweet = re.sub(emojis[k], k, tweet)
    
    return tweet

# Remove single characters surrounded by whitespace(s)

def removeSingleCharacters(tweet):
    pattern = r"\s.\s"
    return re.sub(pattern, " ", tweet)

# Remove extra escape characters for not valid unicode representations

def removeExtraEscapeCharacters(tweet):
    pattern = r"\\(?!u)."
    return re.sub(pattern, "", tweet)

# Replace the unicode escape sequence by the actual character

def replaceUnicodeEscapeSequence(tweet):
    return tweet.encode('utf-8').decode('utf-8')

# Remove specific special characters

def removeSpecialCharacters(tweet):
    pattern = "[\"#\-,%&'’\.$:\(\)\*\+/\[\]\<\>]+"
    return re.sub(pattern, "", tweet)

# Remove numbers

def removeNumbers(tweet):
    pattern = "-?[0-9]+(\.[0-9]*)?"
    return re.sub(pattern, "", tweet)

# Remove tags or mentions

def removeTags(tweet):
    pattern = "@[_a-zA-Z0-9]{1,15}"
    return re.sub(pattern, "", tweet)

# Decode HTML entities

def decode_html_entities(tweet):
    decoded_string = unescape(tweet)
    return decoded_string

# Preprocess the tweet

def preprocessTweet(tweet):
    tweet = removeExtraEscapeCharacters(tweet)
    tweet = replaceUnicodeEscapeSequence(tweet)
    tweet = decode_html_entities(tweet)
    tweet = removeTags(tweet)
    tweet = removeNumbers(tweet)
    tweet = emojis2Text(tweet)
    tweet = removeSpecialCharacters(tweet)
    tweet = removeSingleCharacters(tweet)
    return tweet


df['text'] = df['text'].apply(preprocessTweet)
#df.to_csv('data.csv', index=False)


