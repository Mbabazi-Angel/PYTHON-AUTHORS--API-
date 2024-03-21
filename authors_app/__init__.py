from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authors_app.extensions import db,bcrypt

from authors_app.controllers.auth.auth_controller import auth 


def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate = Migrate(app,db)
    migrate.init_app(app,db)
    bcrypt.init_app(app)

    #importing and registering models
    from authors_app.models.user import User
    from authors_app.models.company import Company
    from authors_app.models.book import Book 

    

    @app.route('/')
    def home ():
      return "hello world"  

    #Registering the blueprint
    app.register_blueprint(auth)
    return app



