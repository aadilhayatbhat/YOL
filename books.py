from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util  
import json

# Function to serialize MongoDB data
def serialize_data(data):
    data['_id'] = str(data['_id'])
    return data

# Define Blueprint
book_api = Blueprint('book_api', __name__)

mongo = PyMongo()

def init_app(app):
    global mongo
    mongo.init_app(app)  

# # Routes for books
# @book_api.route('/', methods=['GET'])
# def get_books():
#     books_cursor = mongo.db.Books.find()
#     books = [serialize_data(book) for book in books_cursor]
#     return jsonify(books)

# @book_api.route('/', methods=['POST'])
# def add_book():
#     data = request.get_json()

#     if data and all(key in data for key in ['bookID', 'title', 'author']):
#         mongo.db.Books.insert_one(data)
#         return jsonify({"message": "Book added successfully"}), 201
#     else:
#         return jsonify({"error": "Missing or invalid field(s)"}), 400

#get book by category 
@book_api.route('/category/<string:category_name>', methods=['GET'])
def get_books_by_category(category_name):
    books_cursor = mongo.db.Books.find({'category': category_name})
    books = [json.loads(json_util.dumps(book)) for book in books_cursor]
    return jsonify(books)

#get book by title
@book_api.route('/title/<string:title>', methods=['GET'])
def get_books_by_title(title):
    
    print('work')
    books_cursor = mongo.db.Books.find({"title":title})
    books_list = [serialize_data(book) for book in books_cursor]
    return jsonify(books_list)

#get book by id 
@book_api.route('/<string:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    
    book = mongo.db.Books.find_one({"bookID": book_id})
    
    # If a book is found, return it
    if book:
        return json.loads(json_util.dumps(book))
    else:
        return jsonify({"error": "Book not found"}), 404

@book_api.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    # Check if all necessary fields are present
    required_fields = ['title', 'author', 'category', 'available', 'pdfUrl', 'audioUrl', 'imageSrc', 'Description']
    if data and all(key in data for key in required_fields):
        mongo.db.Books.insert_one(data)
        return jsonify({"message": "Book added successfully"}), 201
    else:
        return jsonify({"error": "Missing or invalid field(s)"}), 400


@book_api.route('books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    result = mongo.db.Books.delete_one({"bookID": book_id})

    if result.deleted_count:
        return jsonify({"message": "Book deleted successfully"}), 200
    else:
        return jsonify({"error": "Book not found"}), 404
