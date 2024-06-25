from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import click
import sqlalchemy
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from models import db, Tweet
from seeds import *

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tweets.db'

db.init_app(app)

@app.route('/tweet', methods=['POST'])
def save_tweet():
    data = request.get_json()
#    predicted_sentiment = model.predict([data['text']])
#    random_image =  get_random_image_by_sentiment(predicted_sentiment)
    new_tweet = Tweet(
        text=data['text'],
        time=datetime.fromisoformat(data['time']),
        sentiment_id=data['sentiment'],
        #sentiment_id=predicted_sentiment,
        image_id=data['image'],
        #image_id=random_image
        )
    db.session.add(new_tweet)
    db.session.commit()
    return jsonify({'message': 'Tweet saved!'}), 201

@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    tweets = db.session.execute(db.select(Tweet)).scalars().all()
    return jsonify([tweet.to_dict() for tweet in tweets])

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