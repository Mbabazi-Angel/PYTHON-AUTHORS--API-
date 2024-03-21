from flask import Blueprint, request, jsonify
from authors_app.models import user
from flask_bcrypt import Bcrypt
from authors_app.extensions import db  
from authors_app.models.user import User

from authors_app.status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED
import validators

#auth blueprint
auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
bcrypt = Bcrypt()

#user registration
@auth.route('/register', methods=['POST'])
def register():
    try:
        # Extracting request data
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        contact = request.json.get('contact')
        email = request.json.get('email')
        user_type = request.json.get('user_type') if 'user_type' in request.json else "author" # Default to 'author'
        password = request.json.get('password')
        hashed_password = bcrypt.generate_password_hash(password)
        biography = request.json.get('biography', '') if user_type == 'author' else ''

        # Basic input validation
        required_fields = ['first_name', 'last_name', 'contact', 'password', 'email']
        #if not first_name or not last_name or not contact or not password or not email same as;
        if not all(request.json.get(field) for field in required_fields):
            return jsonify({'error': 'All fields are required'}),  HTTP_400_BAD_REQUEST
        

        if user_type == 'author' and not biography:
            return jsonify({'error': 'Enter your author biography'}), HTTP_400_BAD_REQUEST

        if len(password) < 8:
            return jsonify({'error': 'Password is too short'}), HTTP_400_BAD_REQUEST

        if not validators.email(email):
            return jsonify({'error': 'Email is not valid'}),  HTTP_400_BAD_REQUEST
    
        if User.query.filter_by(email=email).first() is not None:
            return jsonify({'error': 'Email already exists'}),HTTP_409_CONFLICT

        if User.query.filter_by(contact=contact).first() is not None:
            return jsonify({'error': 'Contact already exists'}), HTTP_409_CONFLICT
        

        try:
            hashed_password = bcrypt.generate_password_hash(password) #hashing the password

            #creating a new user
            new_user = user(first_name=first_name,last_name=last_name,password=hashed_password,
                            email=email,contact=contact,biography=biography)
           
           #Adding and commiting to the database
            db.session.add(new_user)
            db.session.commit()

            #building a response
            user_name = new_user.get_full_name()


            return jsonify({
                'message':user_name + "has been successfully created as an" + new_user.user_type,
                'user': {
                    'first_name':new_user.first_name,
                    'last_name':new_user.last_name,
                    'email': new_user.email,
                    'contact': new_user.contact,
                    'type':new_user.user_type,
                    'biography':new_user.biography,

                }
            }),HTTP_201_CREATED

        except Exception as e:
            db.session.rollback()
            return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
 

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500