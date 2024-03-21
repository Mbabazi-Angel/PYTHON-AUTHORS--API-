from flask import Blueprint, request, jsonify
from authors_app.models import user
from authors_app.extensions import db
from datetime import datetime

company = Blueprint('company', __name__, url_prefix='/api/v1/company')

@company.route('/register', methods=['POST'])
def register_company():
    try:
        # Extracting request data
       
        name = request.json.get('name')
        origin = request.json.get('origin')
        description = request.json.get('description')

        created_at = request.json.get('created_at')
        updated_at = request.json.get('updated_at')

        # Basic input validation
       

        if not name:
            return jsonify({"error": 'Your company name is required'}), 400

        if not origin:
            return jsonify({"error": 'Your company origin is required'}), 400

        if not description:
            return jsonify({"error": 'Please add a description of your company'}), 400

        # Creating a new user (assuming you have a valid User model)
        user = user(
            first_name='first_name',
            last_name='last_name',
            email='email',
            contact='contact',
            image='image',
            password='password',
            biography='biography',
            user_type='user_type'
        )

        db.session.add(user)
        db.session.commit()

        # Building a response message
        message = f"Account for {user.first_name} {user.last_name} company has been created"
        return jsonify({"message": message}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500