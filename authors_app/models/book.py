from authors_app.extensions import db 
from datetime import datetime



class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(200),nullable=False)
    image = db.Column(db.String(255),nullable=True)
    price = db.Column(db.Integer(),nullable=False)
    price_unit = db.Column(db.String(500),nullable=False,default='UGX')
    publication_date = db.Column(db.Date,nullable=False)
    isbn = db.Column(db.String(30),nullable=True,unique=True)
    genre = db.Column(db.String(50),nullable=False)
    pages = db.Column(db.Integer,nullable=False)
     #Relationship with users
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)

    user = db.relationship('User',backref='book')
    company = db.relationship('Company', backref='book')

    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

    def __init__(self,title,description,image,price,price_unit,publication_date,isbn,genre,pages,user_id,company_id,):
        super(Book,self).__init__()
        self.title = title
        self.description = description
        self.image = image
        self.price = price 
        self.price_unit = price_unit
        self.publication_date = publication_date
        self.isbn = isbn
        self.genre = genre
        self.pages = pages
        self.user_id = user_id
        self.company_id = company_id
    pass 

    def __repr__(self)-> str:
        return f"{self.title} {self.description}"
