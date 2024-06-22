# Preprocessing
import pandas as pd
import re
import nltk
from html import unescape
from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Downloads
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')

data = 'ai_model\preprocessing\SentimentTrain.csv'
df = pd.read_csv(data)

spell = SpellChecker()

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

def spell_check(tweet, corrected_words):
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

# Remove hashtags

def remove_hashtags(text):
    text = re.sub(r'\s*#\w+\b\s*$', '', text)
    text = re.sub(r'\b\s*#(\w+)', r'\1', text)
    text = re.sub(r'^\#(\w+)\b\s*', r'\1', text)
    return text

# Tokenize

def tokenize(text):
    return word_tokenize(text)

# Remove names and possesive terminations

def remove_NNP_and_POS(tweet):
    res = ""
    tagged_words = nltk.pos_tag(tweet.split())
    for word, pos in tagged_words:
        if pos != 'NNP' and pos != 'POS':
            res += word + " "
    return res

# Remove stopwords

def remove_stopwords(tweet):
    res = ""
    stopwords_list = stopwords.words('english')
    for word in tweet.split():
        if word.lower() not in stopwords_list:
            res += word + " "
    return res

# Lemmatize

def lemmatize(tweet):
    lemmatizer = WordNetLemmatizer()
    res = ""
    for word in tweet.split():  
        res += lemmatizer.lemmatize(word) + " "
    return res

# Preprocess the tweet

def preprocessTweet(tweet):
    corrected_words = {}
    tweet = tweet.lower()
    tweet = remove_NNP_and_POS(tweet)
    tweet = replaceUnicodeEscapeSequence(tweet)
    tweet = decodeHTMLEntities(tweet)
    tweet = removeTags(tweet)
    tweet = removeNumbers(tweet)
    tweet = emojis2Text(tweet)
    tweet = removeSpecialCharacters(tweet)
    tweet = removeSingleCharacters(tweet)
    #tweet = spell_check(tweet, corrected_words) # Need to be executed only once, since it takes a very long time
    tweet = remove_hashtags(tweet)
    tweet = remove_stopwords(tweet)
    tweet = lemmatize(tweet)
    return tweet

#df['text'] = df['text'].apply(preprocessTweet)
#df.to_csv('data.csv', index=False)

# Tokenization
#df['tokens'] = df['text'].apply(tokenize)