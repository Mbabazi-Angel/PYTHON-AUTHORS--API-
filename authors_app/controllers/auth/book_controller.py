from flask import Blueprint, request, jsonify
from authors_app.models.book import Book
from authors_app import db
from flask_jwt_extended import jwt_required, get_jwt_identity


book = Blueprint('book', __name__, url_prefix='/api/v1/books')


from authors_app.status_codes import HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_500_INTERNAL_SERVER_ERROR

@book.route('/create', methods=['POST'])
@jwt_required()
def create_book():
    try:
        # Extracting request data
    
        title = request.json.get('title')
        description = request.json.get('description')
        image = request.json.get('image')
        price = request.json.get('price')
        price_unit = request.json.get('price_unit')
        pages = request.json.get('pages')
        publication_date = request.json.get('publication_date')
        isbn = request.json.get('isbn')
        genre = request.json.get('genre')
        user_id = get_jwt_identity()
        company_id = request.json.get('company_id')
        

        # Basic input validation

        if not title:
            return jsonify({"error": 'Your book title is required'}), HTTP_400_BAD_REQUEST

        if not description:
            return jsonify({"error": 'The description is required'}), HTTP_400_BAD_REQUEST

        if not price:
            return jsonify({"error": 'The price is required'}), HTTP_400_BAD_REQUEST

        if not price_unit:
            return jsonify({"error": 'The price_unit is required'}), HTTP_400_BAD_REQUEST

        if not publication_date:
            return jsonify({"error": 'Please input the publication_date'}), HTTP_400_BAD_REQUEST

        if not isbn:
            return jsonify({"error": 'Please input the isbn'}), HTTP_400_BAD_REQUEST

        if not genre:
            return jsonify({"error": 'Please specify the genre'}), HTTP_400_BAD_REQUEST

        # Creating a new book
        new_book = Book(
            title=title,
            description=description,
            image=image,
            price=price,
            price_unit=price_unit,
            pages=pages,
            publication_date=publication_date,
            isbn=isbn,
            genre=genre,
            user_id= user_id,
            company_id= company_id

            
        )

        # Adding and committing to the database
        db.session.add(new_book)
        db.session.commit()

        # Building a response message
        return jsonify({
            "message": f"Book '{new_book.title}', ID '{new_book.id}' has been created",
            'book':{
                'id':new_book.id,
                'title':new_book.title,
                'description': new_book.description,
                'image': new_book.image,
                'price': new_book.price,
                'price_unit': new_book.price_unit,
                'pages': new_book.pages,
                'publication_date': new_book.publication_date,
                'isbn' : new_book.genre,
                'genre': new_book.genre,
                'user_id': new_book.user_id,
                'company_id': new_book.company_id
            }
                        }), HTTP_201_CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
    
   


@book.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    user = get_jwt_identity()
    try:
        book_id = Book.query.filter_by(id=id).first()
        if not book_id:
            return jsonify({'error':'Book does not exist'})
        else:
            db.session.delete(book_id)
            db.session.commit()
            return jsonify({'message': 'Book has been deleted successfully'})
    
    except Exception as e:
        db.session.rollback() 
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR


