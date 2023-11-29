from flask import Blueprint, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

wallpapers_bp = Blueprint('wallpapers', __name__)

def init_app(app):
    global mongo
    mongo = PyMongo(app)

@wallpapers_bp.route('/wallpapers', methods=['GET'])
def get_wallpapers():
    wallpapers = mongo.db.bookwallpapers.find()
    result = []
    for wallpaper in wallpapers:
        # Convert ObjectId to string
        wallpaper['_id'] = str(wallpaper['_id'])
        result.append(wallpaper)
    return jsonify(result)