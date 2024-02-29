from authors_app.extensions import db 
from datetime import datetime



class Company(db.Model):
    __table__ = 'companies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False,unique=True)
    description = db.Column(db.String(100),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

   