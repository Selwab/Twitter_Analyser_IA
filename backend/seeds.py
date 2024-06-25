from models import Sentiment, Image

def seed_sentiment_table(db):
    # Check if the table already has data
    if db.session.execute(db.select(Sentiment)).all() == []:
        sentiments = [
            Sentiment(name="positive"),
            Sentiment(name="negative"),
            Sentiment(name="neutral")
        ]
        db.session.bulk_save_objects(sentiments)
        db.session.commit()
        print("Sentiment table seeded!")
    else:
        print("Sentiment table already seeded!")

def seed_image_table(db):
    # Check if the table already has data
    if db.session.execute(db.select(Sentiment)).all() == []:
        images = [
            Image(
                url="https://th.bing.com/th/id/OIF.4pF0z1FROjIJvy7T8cOhBw?rs=1&pid=ImgDetMain",
                sentiment_id=1 # Positive
                ),
            Image(
                url="https://th.bing.com/th/id/OIP.Ldbqq98Y_WqgXpIVZLfo7AHaGT?w=625&h=532&rs=1&pid=ImgDetMain",
                sentiment_id=2 # Neutral
                ),
            Image(
                url="https://th.bing.com/th/id/OIP.MoeGgyXqne_Vy_vt3KEtRAHaHZ?w=736&h=735&rs=1&pid=ImgDetMain",
                sentiment_id=3 # Negative
                ),
        ]
        db.session.bulk_save_objects(images)
        db.session.commit()
        print("Image table seeded!")
    else:
        print("Image table already seeded!")