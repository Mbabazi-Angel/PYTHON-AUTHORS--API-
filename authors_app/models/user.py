from authors_app.extensions import db 
from datetime import datetime


class User(db.Model):
    __table__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(50),nullable = False)
    last_name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    contact = db.Column(db.Integer,nullable=False,unique=True)
    usertype = db.Column(db.String,nullable=False)
    image = db.Column(db.BLOB,nullable=True)

    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

