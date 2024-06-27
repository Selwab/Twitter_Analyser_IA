import numpy as np
import tensorflow as tf

def predict_sentiment(text, model):
    model_sentiments  = {
        '0': 'negative',
        '1': 'neutral',
        '2': 'positive'
    }

    server_sentiments = {
        'positive': 1,
        'neutral': 2,
        'negative': 3
    }

    predicted = model.predict(tf.convert_to_tensor([text]))
    max_index = np.argmax(predicted)
    return server_sentiments[model_sentiments[str(max_index)]]