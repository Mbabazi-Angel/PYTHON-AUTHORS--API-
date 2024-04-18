from flask import Flask, jsonify  
from flask_migrate import Migrate
from authors_app.extensions import bcrypt,jwt,db 
from flasgger import Swagger

from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_from_directory
import os 

from authors_app.controllers.auth.auth_controller import auth 
from authors_app.controllers.auth.company_controller import company 
from authors_app.controllers.auth.book_controller import book




def create_app():
    app = Flask(__name__)

  
    app.config.from_object('config.Config')


    #initialise database
    db.init_app(app)
    migrate = Migrate(app,db)
    migrate.init_app(app,db)
    bcrypt.init_app(app)

    jwt.init_app(app)

    #importing and registering models
    from authors_app.models.user import User
    from authors_app.models.company import Company
    from authors_app.models.book import Book 

    # Serve Swagger JSON file
    @app.route('/swagger.json')
    def serve_swagger_json():
       try:
          return send_from_directory(os.path.dirname(os.path.abspath(__file__)),'swagger.json')
       
       except FileNotFoundError:
          return jsonify({"message": "Swagger JSON file not found"}),404
       
       #Swagger UI configuration 
    SWAGGER_URL = '/api/docs' #URL for exposing Swagger UI(without trailing)
    API_URL = '/swagger.json'

    #Create swagger UI blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
       SWAGGER_URL,
       API_URL,
       config = {
          'app_name': "authors_app"
       }
    )



    @app.route('/')
    def home ():
      return "hello world"  

    #Registering the blueprint
    app.register_blueprint(auth)
    app.register_blueprint(company)
    app.register_blueprint(book)

    return app






