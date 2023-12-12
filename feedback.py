from flask import Blueprint, request, jsonify
from pymongo import MongoClient


feedback_bp = Blueprint('feedback_bp', __name__)

client = MongoClient('mongodb+srv://serveradmin:Password123@cluster0.4qwnmiz.mongodb.net/Librarymanagement?retryWrites=true&w=majority')
db = client['Librarymanagement'] 
feedback_collection = db.feedback

@feedback_bp.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        data = request.get_json()
        name = data['name']
        phone = data['phone']
        email = data['email']
        feedback = data['feedback']
        
        feedback_document = {
            "name": name,
            "phone": phone,
            "email": email,
            "feedback": feedback
        }
        feedback_collection.insert_one(feedback_document)
        
        return 'Feedback submitted successfully', 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@feedback_bp.route('/get_feedback', methods=['GET'])
def get_feedback():
    feedback_data = feedback_collection.find()
    feedback_list = [feedback for feedback in feedback_data]
    for feedback in feedback_list:
        feedback.pop('_id', None)
    return jsonify(feedback_list)

# This function registers the Blueprint to the app
def init_app(app):
    pass
