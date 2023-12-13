from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

# Import  initialization functions 
from student import init_app as student_init_app, student_api
from books import init_app as book_init_app, book_api
from login import init_app as login_init_app, login_api
from category import init_app as category_init_app, category_api
from feedback import init_app as feedback_init_app,feedback_bp
from wallpapers import init_app as wallpapers_init_app, wallpapers_bp

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://serveradmin:Password123@cluster0.4qwnmiz.mongodb.net/Librarymanagement?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
def login():
    return render_template('login.html')

# Initialize
student_init_app(app)
book_init_app(app)
login_init_app(app)
category_init_app(app)
feedback_init_app(app)
wallpapers_init_app(app) 



app.secret_key = "your_secret_key_here"

# Register Blueprints for other modules
app.register_blueprint(student_api, url_prefix='/student')
app.register_blueprint(book_api, url_prefix='/books')
app.register_blueprint(login_api, url_prefix='/login')
app.register_blueprint(category_api, url_prefix='/category')
app.register_blueprint(feedback_bp, url_prefix='/feedback')
app.register_blueprint(wallpapers_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)

CORS(app)