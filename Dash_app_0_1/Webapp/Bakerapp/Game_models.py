from . import db
import datetime

class Heroes(db.Model):
    """Table representing hero data in the game"""

    __tablename__ = "Heroes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), default="NULL")
    localized_name = db.Column(db.String(128), default="NULL")
    primary_attr = db.Column(db.String(128), default="NULL")
    attack_type = db.Column(db.String(128), default="NULL")
    
    def __str__(self):
        return self.Name

class Items(db.Model):
    """Table representing item data in the game"""

    __tablename__ = "Items"
    Item_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(128), default="NULL")

    def __str__(self):
        return self.Name