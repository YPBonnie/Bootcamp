from flask import Blueprint, jsonify
from ..models import Tweet, db

bp = Blueprint('tweets', __name__, url_prefix='/tweets')
#Decorator takes path and list of HTTP verbs
@bp.route('', methods=['GET'])
def index():
    #ORM SELECT query
    tweets = Tweet.query.all()
    result = []
    for t in tweets:
        result.append(t.serialize())
    return jsonify(result)


# Task 3: Implement Tweets show endpoint
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Tweet.query.get_or_404(id)
    return jsonify(t.serialize())

#Task 5: Implement Tweets delete endpoint
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    t = Tweet.query.get_or_404(id)
    try:
        db.session.delete(t)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
    
@bp.route('/<int:id>/liking_users', methods=['GET'])
def liking_users(id: int):
    t = Tweet.query.get_or_404(id)
    result = []
    for u in t.liking_users:
        result.append(u.serialize())
    return jsonify(result)
