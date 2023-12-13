from flask import Blueprint, request, jsonify, session
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_cors import CORS

client = MongoClient('mongodb+srv://serveradmin:Password123@cluster0.4qwnmiz.mongodb.net/Librarymanagement?retryWrites=true&w=majority')
db = client['Librarymanagement'] 


# Define Blueprint
login_api = Blueprint('login_api', __name__)

# Create a function for initializing the blueprint with the app instance
def init_app(app):
    mongo = PyMongo(app)

    @login_api.route('/', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get('email', '')
        password = data.get('password', '')

        student = mongo.db.students.find_one({"email": email})

        if student:
            if student['password'] == password:  # Compare plain text passwords
                session['user_id'] = str(student['_id'])  # Storing user ID in session
                if student.get('isAdmin'):
                    return jsonify({"status": "admin"}), 200  # Admin user
                else:
                    return jsonify({"status": "user"}), 200  # Regular user
            else:
                return jsonify({"status": "failure", "message": "Invalid credentials"}), 401
        else:
            return jsonify({"status": "failure", "message": "User not found, please sign up."}), 401
