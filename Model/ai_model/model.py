from spellchecker import SpellChecker
import pandas as pd
import matplotlib.pyplot as plt
import contractions
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, TextVectorization, Flatten
from tensorflow.keras.layers import Bidirectional
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from textattack.augmentation import EasyDataAugmenter
import re
from html import unescape
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import emoji

# Downloads
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')

path = 'ai_model\preprocessing\SentimentTrain.csv'
df = pd.read_csv(path)

eda_aug = EasyDataAugmenter()
def expand_category(csv_file, label_to_expand, n_duplicates, output_file):
    # Load the CSV data
    df = pd.read_csv(csv_file)

    # Identify rows with the specified label
    rows_to_expand = df[df['label'] == label_to_expand]

    # List to store the new rows
    new_rows = []

    for _, row in rows_to_expand.iterrows():
        for _ in range(n_duplicates):
            modified_text = eda_aug.augment(row['text'])
            new_row = {'text': modified_text, 'label': row['label']}
            new_rows.append(new_row)

    # Create a DataFrame from the new rows
    new_rows_df = pd.DataFrame(new_rows)

    # Concatenate the original dataframe with the new rows dataframe
    expanded_df = pd.concat([df, new_rows_df], ignore_index=True)

    # Save the expanded data back to a CSV file
    expanded_df.to_csv(output_file, index=False)

expand_category(df, 0, 2, 'expanded_output.csv')

# Display a graphic with the sentiment data distribution. We can see that there is the same number of tweets for each tweet

path = 'ai_model\preprocessing\expanded_output.csv'
df = pd.read_csv(path)

ax = df['label'].value_counts().plot(kind='bar', title='Sentiment Distribution')
ax.set_xlabel('Sentiment')
ax.set_ylabel('Count')
plt.show()

# FUNCTIONS FOR TEXT PREPROCESSING

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
    pattern = r"[\"#\-,%&'’\.$:\(\)\*\+/\[\]\<\>\\\?\!]+"
    return re.sub(pattern, "", tweet)

# Remove numbers

def removeNumbers(tweet):
    pattern = "-?[0-9]+(\.[0-9]*)?"
    return re.sub(pattern, "", tweet)

# Expanding contractions
def expand_contractions(text):
    expanded_words = [contractions.fix(word) for word in text.split()]
    expanded_text = ' '.join(expanded_words)
    return expanded_text


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

def demojize(tweet):
  return(emoji.demojize(tweet))

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
        #if pos != 'NNP' and pos != 'POS':
        if pos != 'POS':
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
    tweet = remove_NNP_and_POS(tweet)
    tweet = tweet.lower()
    tweet = expand_contractions(tweet)
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

# APPLY ALL PREPROCESSING FUNCTIONS TO THE DATASET AND SAVE INTO A NEW .CSV FILE
path = 'ai_model\preprocessing\expanded_output.csv'
df['cured']= df['text'].apply(preprocessTweet)
df.to_csv('cured_emotion_data.csv', index=False)

# Create the text vectorization layer. This layers includes internally the following steps:
# Standardize each example (usually lowercasing + punctuation stripping)
# Split each example into substrings (usually words)
# Recombine substrings into tokens (usually ngrams)
# Index tokens (associate a unique int value with each token)
# Transform each example using this index, either into a vector of ints or a dense float vector.

max_tokens = 3000  # Maximum vocab size.


vectorize_layer = TextVectorization(
    max_tokens=max_tokens,
    output_mode='int'
    )

vectorize_layer.adapt(list(df['cured'].values))

print(vectorize_layer.get_vocabulary())
print(vectorize_layer.vocabulary_size())

# Apply one=hot encoding to the labels
label_as_vector = to_categorical(df['label'].values)

# Split the data for training and testing
x_train, x_test, y_train, y_test = train_test_split(df['cured'].values, label_as_vector, test_size=0.3, random_state=13)
#print(x_train)

model = tf.keras.Sequential([
    vectorize_layer,
    tf.keras.layers.Embedding(max_tokens, 128),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Bidirectional(LSTM(128, return_sequences=True, activation='tanh')),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Bidirectional(LSTM(128, activation='tanh')),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',      # Metric to monitor
    patience=3,              # Number of epochs to wait for improvement
    restore_best_weights=True # Restore model weights from the epoch with the best value of the monitored quantity
)
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',     # Metric to monitor
    factor=0.2,             # Factor by which to reduce the learning rate
    patience=2,             # Number of epochs with no improvement after which learning rate will be reduced
    min_lr=0.0001           # Lower bound on the learning rate
)

#model train
model_history = model.fit(x_train, y_train, epochs=20, batch_size=32, validation_data=(x_test, y_test),callbacks=[early_stopping, reduce_lr])

score = model.evaluate(x_test, y_test)
#print(model_history.history.keys())

print("Test score:", score[0])
print("Test accuracy:", score[1])

plt.plot(model_history.history['accuracy'])
plt.plot(model_history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(model_history.history['loss'])
plt.plot(model_history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')

print(model.predict(x_test))
print(y_test)

model.save('TweetAnalysis')
zip -r /content/TweetAnalysis.zip /content/TweetAnalysis