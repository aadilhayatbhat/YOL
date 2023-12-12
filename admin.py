from flask import Blueprint, request, redirect, render_template
from pymongo import MongoClient
import hashlib

# Initialize MongoDB client
client = MongoClient('mongodb+srv://serveradmin:<Password123>@cluster0.4qwnmiz.mongodb.net/')
db = client['Librarymanagement']

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admin', methods=['GET'])
def admin_page():
    return render_template('admin.html')

@admin_bp.route('/admin_login', methods=['POST'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    admin = db.admin.find_one({'username': username, 'password': hashed_password})

    if admin:
        return redirect('/admin')
    else:
        return "Invalid credentials"

@admin_bp.route('/add_book', methods=['POST'])
def add_book():
    book_id = request.form['book_id']
    title = request.form['title']
    author = request.form['author']

    book_data = {'book_id': book_id, 'title': title, 'author': author}
    db.books.insert_one(book_data)

    return redirect('/admin')
