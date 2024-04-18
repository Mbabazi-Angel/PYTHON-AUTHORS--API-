from authors_app.extensions import db 
from datetime import datetime
 

from authors_app.extensions import bcrypt

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(50),nullable = False) 
    last_name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    contact = db.Column(db.String(100),nullable=False,unique=True)
    user_type = db.Column(db.String(50),nullable=False,default='author')
    image = db.Column(db.String(255),nullable=True)
    biography = db.Column(db.Text(),nullable=True)

    password = db.Column(db.String(128),nullable=False) #Store the hashed password

    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

    def __init__(self, first_name,last_name,email,contact,password,user_type,image,biography): 
        super(User,self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.password = password
        self.usertype = user_type
        self.image = image
        self.biography = biography
    pass 

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def set_password(self,password):
        self._password = bcrypt.generate_password_hash(password).decode('url')
