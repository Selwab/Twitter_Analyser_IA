from models import db, Image
import random

def get_image_url(image_id):
    image = db.session.execute(db.select(Image).where(Image.id==image_id)).scalar_one()
    return image.url

def get_random_image_by_sentiment(sentiment_id):
    images = db.session.execute(db.select(Image).where(Image.sentiment_id==sentiment_id)).scalars().all()
    random_index = random.randint(0, len(images)-1)
    return images[random_index].id