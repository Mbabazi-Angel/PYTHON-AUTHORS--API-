from authors_app import db 



class Company(db.Model):
    __table__ = 'company'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False,unique=True)
    description = db.Column(db.String(100),nullable=False)
    user_Id = db.Column(db.Integer, foreign_key=True)