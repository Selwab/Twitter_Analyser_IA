# Preprocessing
import pandas as pd
import re
from html import unescape
from spellchecker import SpellChecker

spell = SpellChecker()

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

# Replace unicode sequences

def replaceUnicodeEscapeSequence(tweet):
    replacements = {
        r'\\u2019': "'",
        r'\\u002c': ",",
    }
    
    for unicode_char, replacement in replacements.items():
        tweet = re.sub(unicode_char, replacement, tweet)
    
    return tweet

# Remove specific special characters

def removeSpecialCharacters(tweet):
    pattern = r"[\"#\-,%&'’\.$:\(\)\*\+/\[\]\<\>\\]+"
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

def decodeHTMLEntities(tweet):
    decoded_string = unescape(tweet)
    return decoded_string

# Spell check
corrected_words = {}

def spell_check(tweet):
  corrected_text = ""

  for word in tweet.split():
    word = word.lower() 
    if word not in corrected_words:
      correction = spell.correction(word)
    
      if correction is not None:
        corrected_words[word] = correction
        corrected_text += spell.correction(word) + " "
      else:
        corrected_text += word + " "
    else:
      corrected_text += corrected_words[word] + " "

  return corrected_text

# Preprocess the tweet

def preprocessTweet(tweet):
    tweet = tweet.lower()
    tweet = replaceUnicodeEscapeSequence(tweet)
    tweet = decodeHTMLEntities(tweet)
    tweet = removeTags(tweet)
    tweet = removeNumbers(tweet)
    tweet = emojis2Text(tweet)
    tweet = removeSpecialCharacters(tweet)
    tweet = removeSingleCharacters(tweet)
    #tweet = spell_check(tweet) # Need to be executed only once, since it takes a very long time
    return tweet


#df['text'] = df['text'].apply(preprocessTweet)
#df.to_csv('data.csv', index=False)