import tensorflow as tf
from tensorflow import keras
import numpy as np
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

print(tf.version.VERSION)

# Load the model
model = tf.keras.models.load_model('Model/TweetAnalyzer_2_16_1.keras')

# Check its architecture
model.summary()

# Load the tokenizer (assuming it was saved during training)
tokenizer = word_tokenize
# Predict
predictions = model.predict(tf.convert_to_tensor(['please end this suffering']))
print(predictions)
