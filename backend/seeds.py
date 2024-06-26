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
    if db.session.execute(db.select(Image)).all() == []:
        images = [
            # Positive
            Image(
                url="https://th.bing.com/th/id/OIF.4pF0z1FROjIJvy7T8cOhBw?rs=1&pid=ImgDetMain",
                sentiment_id=1 
                ),
            Image(
                url="https://media.tenor.com/jOP7VJ_YfqgAAAAM/cheers.gif",
                sentiment_id=1 
                ),
            Image(
                url="https://lumiere-a.akamaihd.net/v1/images/image_2c3e486d.jpeg?region=0,623,1080,1297",
                sentiment_id=1 
                ),
             # Neutral
            Image(
                url="https://th.bing.com/th/id/OIP.Ldbqq98Y_WqgXpIVZLfo7AHaGT?w=625&h=532&rs=1&pid=ImgDetMain",
                sentiment_id=2
                ),
            Image(
                url="https://i.pinimg.com/originals/76/5a/2b/765a2b88d614f5cbe4fdf4c74c554ee9.png",
                sentiment_id=2
                ),
            Image(
                url="https://ih1.redbubble.net/image.2595320116.9420/flat,750x,075,f-pad,750x1000,f8f8f8.jpg",
                sentiment_id=2
                ),
            Image(
                url="https://i.pinimg.com/564x/f0/2b/ed/f02bed84317f6e41a5b0118348173512.jpg",
                sentiment_id=2
                ),
            # Negative
            Image(
                url="https://th.bing.com/th/id/OIP.MoeGgyXqne_Vy_vt3KEtRAHaHZ?w=736&h=735&rs=1&pid=ImgDetMain",
                sentiment_id=3
                ),
            Image(
                url="https://i.pinimg.com/originals/31/c4/c1/31c4c134f5edc3d46084fa85586f3697.jpg",
                sentiment_id=3
                ),
            Image(
                url="https://i1.sndcdn.com/artworks-dcZZznwvCIjxzVdh-Ia2kPw-t500x500.jpg",
                sentiment_id=3
                )
    
        ]
        db.session.bulk_save_objects(images)
        db.session.commit()
        print("Image table seeded!")
    else:
        print("Image table already seeded!")