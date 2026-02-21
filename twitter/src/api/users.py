from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Tweet, likes_table
import hashlib
import secrets

def scramble(password: str):
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('users', __name__, url_prefix='/users')

#Decorator takes path and list of HTTP verbs
@bp.route('', methods=['GET'])
def index():
    #ORM SELECT query
    users = User.query.all()
    result = []
    for u in users:
        result.append(u.serialize())
    return jsonify(result)

# Task 3: Implement Users show endpoint
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())

# Task 4: Implement Users create endpoint
@bp.route('', methods=['POST'])
def create():
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    
    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)
    
    #create a new user object
    u = User(
        username = request.json['username'],
        password = scramble(request.json['password'])
    )

    try:
        db.session.add(u)
        db.session.commit()
        return jsonify(u.serialize())
    except Exception as e:
        return abort(400, description="Username already taken")

#Update a user's information
@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    u = User.query.get_or_404(id)
    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        u.username = request.json['username']
    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        u.password = scramble(request.json['password'])
    
    db.session.commit()
    return jsonify(u.serialize())

# Task 5: Implement Users delete endpoint
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u) # Delete the user
        db.session.commit() # Save the change
        return jsonify(True)
    except:
        return jsonify(False)

# Task 6: Implement liking a tweet
@bp.route('/<int:id>/liking_tweet', methods=['POST'])
def liking_tweet(id: int):
    # Ensure the target tweet_id is in the request body
    if 'tweet_id' not in request.json:
        return abort(400)
    
    u = User.query.get_or_404(id)
    t = Tweet.query.get_or_404(request.json['tweet_id'])
    
    # SQLAlchemy many-to-many magic: 
    # Appending the tweet object to the user's liked_tweets list 
    # automatically inserts a row into the hidden likes_table.
    u.liked_tweets.append(t)
    
    try:
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)