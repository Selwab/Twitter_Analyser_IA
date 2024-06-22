# Preprocessing
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords

# Downloads
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

data = 'ai_model\preprocessing\SentimentTrain.csv'
df = pd.read_csv(data)

def remove_hashtags(text):
    text = re.sub(r'\s*#\w+\b\s*$', '', text)
    text = re.sub(r'\b\s*#(\w+)', r'\1', text)
    text = re.sub(r'^\#(\w+)\b\s*', r'\1', text)
    return text

def tokenize(text):
    return word_tokenize(text)

def remove_NNP_and_POS(tokens):
    res = []
    tagged_words = nltk.pos_tag(tokens)
    for word, pos in tagged_words:
        if pos != 'NNP' and pos != 'POS':
            res.append(word)
    return res

def remove_stopwords(tokens):
    res = []
    stopwords_list = stopwords.words('english')
    for word in tokens:
        if word.lower() not in stopwords_list:
            res.append(word)
    return res

# Delete Hashtags
df['text'] = df['text'].apply(remove_hashtags)
print("No HASH \n", df['text'].iloc[11])
print("No HASH \n", df['text'].iloc[64])
print("No HASH \n", df['text'].iloc[36])

# Tokenization
df['tokens'] = df['text'].apply(tokenize)
print("All Tokens: \n", df['tokens'].iloc[1])

#Remove proper nouns and possessive endings
df['tokens'] = df['tokens'].apply(remove_NNP_and_POS)
print("Del POS: \n", df['tokens'].iloc[1])

# Stopwords
df['tokens'] = df['tokens'].apply(remove_stopwords)
print("Del STOP: \n", df['tokens'].iloc[0:9])