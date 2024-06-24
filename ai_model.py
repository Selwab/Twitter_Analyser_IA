import pandas as pd
from sklearn.model_selection import train_test_split

data = 'ai_model\preprocessing\SentimentTrain.csv'
df = pd.read_csv(data)

x_train, x_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.3, random_state=13)