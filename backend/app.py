from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from models import db, Tweet, Image
from seeds import *
import random

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tweets.db'
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

db.init_app(app)

def get_image_url(image_id):
    image = db.session.execute(db.select(Image).where(Image.id==image_id)).scalar_one()
    return image.url

def get_random_image_by_sentiment(sentiment_id):
    images = db.session.execute(db.select(Image).where(Image.sentiment_id==sentiment_id)).scalars().all()
    random_index = random.randint(0, len(images)-1)
    return images[random_index].id

@app.route('/tweet', methods=['POST'])
def save_tweet():
    data = request.get_json()
#    predicted_sentiment = model.predict([data['text']])
    predicted_sentiment=1
    random_image =  get_random_image_by_sentiment(predicted_sentiment)
    new_tweet = Tweet(
        text=data['text'],
        time=datetime.fromisoformat(data['time']),
        sentiment_id=predicted_sentiment,
        image_id=random_image
        )
    db.session.add(new_tweet)
    db.session.commit()

    tweet_dto = {
        'id': new_tweet.id,
        'text': new_tweet.text,
        'sentiment_id': new_tweet.sentiment_id,
        'image_url': get_image_url(new_tweet.image_id),
        'time': new_tweet.time
    }

    return jsonify(tweet_dto), 201

@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    tweets = db.session.execute(db.select(Tweet)).scalars().all()
    tweets_with_images = []
    for tweet in tweets:
        tweet_to_dict = tweet.to_dict()
        tweet_to_dict['image_url'] = get_image_url(tweet.image_id)
        tweets_with_images.append(tweet_to_dict)
    return jsonify(tweets_with_images)

@app.route('/tweet', methods=['GET'])
def get_tweet_by_id():
    tweet_id = int(request.args.get('id'))
    tweet = db.session.execute(db.select(Tweet).where(Tweet.id == tweet_id)).scalar()
    if tweet is None:
        return jsonify({'error': 'Tweet not found'}), 404

    return jsonify(tweet.to_dict())

@app.route('/tweets/sentiment', methods=['GET'])
def get_tweets_by_sentiment():
    sentiment_id = int(request.args.get('id'))
    tweets = db.session.execute(db.select(Tweet).where(Tweet.sentiment_id == sentiment_id)).scalars().all()
    return jsonify([tweet.to_dict() for tweet in tweets])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_sentiment_table(db)    
        seed_image_table(db)
    app.run(debug=True, port=8000)

