from flask import Flask 

from authors_app.extensions import db,migrate 


def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app,db)

    from authors_app.models.user import use
    from authors_app.models.company import Company
    from authors_app.models.book import Book



    @app.route('/')
    def home ():
      return "hello world"  


    return app



