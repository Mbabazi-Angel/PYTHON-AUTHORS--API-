from authors_app import db 



class Boook(db.Model):
    __table__ = 'book'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(200),nullable=False)
    image = db.Column(nullable=False)
    price = db.Column(db.Integer,nullable=False)
    number_of_pages = db.Column(db.Integer,nullable=False)

