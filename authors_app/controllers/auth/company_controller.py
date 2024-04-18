from flask import Blueprint, request, jsonify
from authors_app.models.company import Company 
from authors_app.extensions import db
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from authors_app.status_codes import HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_500_INTERNAL_SERVER_ERROR

company = Blueprint('company', __name__, url_prefix='/api/v1/companies')

@company.route('/create', methods=['POST'])
@jwt_required()
def create_company():
    try:
        # Extracting request data
       
        name = request.json.get('name')
        origin = request.json.get('origin')
        description = request.json.get('description')
        user_id = get_jwt_identity()
        
        # Basic input validation
        

        if not name:
            return jsonify({"error": 'Your company name is required'}), HTTP_400_BAD_REQUEST

        if not origin:
            return jsonify({"error": 'Your company origin is required'}), HTTP_400_BAD_REQUEST

        if not description:
            return jsonify({"error": 'Please add a description of your company'}), HTTP_400_BAD_REQUEST
        
        if Company.query.filter_by(name=name).first():
            return jsonify({"error": 'Company name already exists'})  

        # Creating a new user (assuming you have a valid User model)
        new_company = Company(
            name=name,
            origin=origin,
            description=description,
            user_id = user_id
        )

        db.session.add(new_company)
        db.session.commit()

        # Building a response message
        message = f"{new_company.name} has been successfully added"
        return jsonify({
            "message": message,
            'company':{
                'id':new_company.id,
                'name':new_company.name,
                'origin': new_company.origin,
                'description': new_company.description,
                'user_id': new_company.user_id 
            }
            }), HTTP_201_CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
    
@company.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_company(id):
    user = get_jwt_identity()
    try:
        company_id = Company.query.filter_by(id=id,user_id=user).first()
        if not company_id:
            return jsonify({'error':'Company does not exist'})
        else:
            db.session.delete(company_id)
            db.session.commit()
            return jsonify({'message': 'Company has been deleted successfully'})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
        

        