from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Sentiment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Sentiment {self.name}>'


class Image(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(db.String(200), nullable=False)
    sentiment_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('sentiment.id'), nullable=False)

    def __repr__(self):
        return f'<Image {self.url}>'


class Tweet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(db.Text, nullable=False)
    time: Mapped[datetime] = mapped_column(db.DateTime, nullable=False, default=datetime.utcnow)
    sentiment_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('sentiment.id'), nullable=False)
    image_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('image.id'), nullable=False)

    def __repr__(self):
        return f'<Tweet {self.text[:20]}>'
    
    def to_dict(self):
         return {
            'id': self.id,
            'text': self.text,
            'time': self.time.isoformat(),
            'sentiment_id': self.sentiment_id,
            'image_id': self.image_id
        }

