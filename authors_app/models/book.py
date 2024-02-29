from authors_app.extensions import db 
from datetime import datetime


class Book(db.Model):
    __table__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(200),nullable=False)
    image = db.Column(db.BLOB,nullable=False)
    price = db.Column(db.Integer,nullable=False)
    number_of_pages = db.Column(db.Integer,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    company_id = db.Column(db.Integer,db.ForeignKey('companies.id'))

    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

