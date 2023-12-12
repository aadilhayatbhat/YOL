from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient

client = MongoClient('mongodb+srv://serveradmin:Password123@cluster0.4qwnmiz.mongodb.net/Librarymanagement?retryWrites=true&w=majority')
db = client['Librarymanagement'] 


# Function to serialize MongoDB data
def serialize_data(data):
    data['_id'] = str(data['_id'])
    return data

# Initialize Blueprint
student_api = Blueprint('student_api', __name__)

# Inject the mongo instance during Blueprint registration in the main app
def init_app(app):
    global mongo
    mongo = PyMongo(app)

# Define routes for students
@student_api.route('/', methods=['GET'])
def get_students():
    students_cursor = mongo.db.students.find()
    students = [serialize_data(student) for student in students_cursor]
    return jsonify(students)

@student_api.route('/', methods=['POST'])
def add_student():
    data = request.get_json()
    if data and all(key in data for key in ['studentID', 'name', 'phoneNo', 'email']):
        mongo.db.students.insert_one(data)
        return jsonify({"message": "Student added successfully"}), 201
    else:
        return jsonify({"error": "Missing or invalid field(s)"}), 400
