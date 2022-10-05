from . import db
import datetime

class Heroes(db.Model):
    """Table representing hero data in the game"""

    __tablename__ = "Heroes"
    Hero_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(128), default="NULL")

    def __str__(self):
        return self.Name

class Items(db.Model):
    """Table representing item data in the game"""

    __tablename__ = "Items"
    Item_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(128), default="NULL")

    def __str__(self):
        return self.Name