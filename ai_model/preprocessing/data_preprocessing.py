# Preprocessing
import pandas as pd
import re

data = 'ai_model\preprocessing\SentimentTrain.csv'
df = pd.read_csv(data)

def remove_hashtags(text):
    text = re.sub(r'\s*#\w+\b\s*$', '', text)
    text = re.sub(r'\b\s*#(\w+)', r'\1', text)
    text = re.sub(r'^\#(\w+)\b\s*', r'\1', text)
    return text

# Delete Hashtags
df['text'] = df['text'].apply(remove_hashtags)
print("No HASH \n", df['text'].iloc[11])
print("No HASH \n", df['text'].iloc[64])
print("No HASH \n", df['text'].iloc[36])