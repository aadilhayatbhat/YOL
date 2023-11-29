from flask import Blueprint, jsonify
from pymongo import MongoClient

category_api = Blueprint('category_api', __name__)

client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string
db = client['Librarymanagement']

@category_api.route('/categories', methods=['GET'])
def get_categories():
    categories_cursor = db.categories.find({}, {'_id': 0})  # Exclude _id field from the result
    categories = [category for category in categories_cursor]
    return jsonify(categories)

def init_app(app):
    # Any initialization can be put here
    pass


