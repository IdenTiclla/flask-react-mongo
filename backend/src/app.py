from flask import Flask, request, jsonify
from flask.json import jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreactdb'
mongo = PyMongo(app)

db = mongo.db.users

@app.route('/users', methods=['GET'])
def get_users():
    return 'received'

@app.route('/users', methods=['POST'])
def create_user():
    id = db.insert({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    })
    return jsonify(str(ObjectId(id)))

@app.route('/users/<id>', methods=['POST'])
def get_user(id):
    return 'received'

@app.route('/users/<id>', methods=['GET'])
def delete_user():
    return 'received'

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    return 'received'

if __name__ == "__main__":
    app.run(debug=True)
