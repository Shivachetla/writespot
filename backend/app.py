from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, User, Story, Book
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quietude.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key' # Change this in production

db.init_app(app)
jwt = JWTManager(app)

# Routes

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token, user=user.to_dict()), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/stories', methods=['GET'])
def get_stories():
    category = request.args.get('category')
    if category:
        stories = Story.query.filter_by(category=category).all()
    else:
        stories = Story.query.all()
    return jsonify([story.to_dict() for story in stories])

@app.route('/api/stories', methods=['POST'])
@jwt_required()
def create_story():
    current_user_username = get_jwt_identity()
    user = User.query.filter_by(username=current_user_username).first()
    
    data = request.get_json()
    new_story = Story(
        title=data['title'],
        content=data['content'],
        excerpt=data.get('excerpt', ''),
        category=data.get('category', 'General'),
        read_time=data.get('read_time', '5 min read'),
        image_url=data.get('image_url', ''),
        author_id=user.id
    )
    db.session.add(new_story)
    db.session.commit()
    
    return jsonify(new_story.to_dict()), 201

@app.route('/api/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/api/users/<username>', methods=['GET'])
def get_user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return jsonify(user.to_dict())

# Serve Frontend
@app.route('/')
def index():
    return app.send_static_file('homepage/code.html')

@app.route('/<path:path>')
def serve_static(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
