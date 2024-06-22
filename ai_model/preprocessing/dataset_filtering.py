import pandas as pd
import matplotlib.pyplot as plt

path = 'ai_model\preprocessing\SentimentTrain.csv'
df = pd.read_csv(path)

positives = 0
negatives = 0
neutrals = 0
max_sentiment_samples = 3500
df2 = pd.DataFrame(
    {
        'text': [],
        'label': [] 
    }
)

for row in df.iterrows():
  if row[1]['label'] == 0 and negatives < max_sentiment_samples :
    negatives += 1
    df2 = df2._append({'text': row[1]['text'], 'label': row[1]['label']}, ignore_index=True)
  elif row[1]['label'] == 2 and positives < max_sentiment_samples :
    positives += 1
    df2 = df2._append({'text': row[1]['text'], 'label': row[1]['label']}, ignore_index=True)
  elif row[1]['label'] == 1 and neutrals < max_sentiment_samples:
    neutrals += 1
    df2 = df2._append({'text': row[1]['text'], 'label': row[1]['label']}, ignore_index=True)

  if neutrals >= max_sentiment_samples and positives >= max_sentiment_samples and negatives >= max_sentiment_samples:
    break

ax = df2['label'].value_counts().plot(kind='bar', title='Sentiment Distribution')
ax.set_xlabel('Sentiment')
ax.set_ylabel('Count')
plt.show()

df2.to_csv('dataset.csv', index=False)
