from flask import Blueprint, request, jsonify
from authors_app.models import book
from authors_app import db

book = Blueprint('book', __name__, url_prefix='/api/v1/book')

@book.route('/register', methods=['POST'])
def register_book():
    try:
        # Extracting request data
        id = request.json.get('id')
        title = request.json.get('title')
        description = request.json.get('description')
        image = request.json.get('image')
        price = request.json.get('price')
        price_unit = request.json.get('price_unit')
        pages = request.json.get('pages')
        publication_date = request.json.get('publication_date')
        isbn = request.json.get('isbn')
        genre = request.json.get('genre')
        created_at = request.json.get('created_at')
        updated_at = request.json.get('updated_at')

        # Basic input validation
        if not id:
            return jsonify({"error": 'Your book ID is required'}), 400

        if not title:
            return jsonify({"error": 'Your book title is required'}), 400

        if not description:
            return jsonify({"error": 'The description is required'}), 400

        if not price:
            return jsonify({"error": 'The price is required'}), 400

        if not price_unit:
            return jsonify({"error": 'The price_unit is required'}), 400

        if not publication_date:
            return jsonify({"error": 'Please input the publication_date'}), 400

        if not isbn:
            return jsonify({"error": 'Please input the isbn'}), 400

        if not genre:
            return jsonify({"error": 'Please specify the genre'}), 400

        # Creating a new book
        new_book = book(
            id=id,
            title=title,
            description=description,
            image=image,
            price=price,
            price_unit=price_unit,
            pages=pages,
            publication_date=publication_date,
            isbn=isbn,
            genre=genre,
            created_at=created_at,
            updated_at=updated_at
        )

        # Adding and committing to the database
        db.session.add(new_book)
        db.session.commit()

        # Building a response message
        return jsonify({"message": f"Book '{new_book.title}', ID '{new_book.id}' has been uploaded"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500