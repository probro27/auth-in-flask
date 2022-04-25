## Make a rest API that authenticates users:

## Routes to be implemented:
# /auth/register
# /auth/login

from flask import Flask, request, jsonify
import register
import login
import jwt
import os
from dotenv import load_dotenv
load_dotenv()
token_secret = os.getenv('TOKEN_SECRET')

app = Flask(__name__)

@app.route('/', methods= ['GET'])
def home():
    data = "hello world"
    return jsonify({'data': data})

@app.route('/auth/register', methods=['POST'])
def register_route():
    data = request.get_json()
    print(data)
    username = data['username']
    password = data['password']
    
    token = register.register_func(username, password)

    if token != False:
        return jsonify({'token': token, 'message': 'user registered successfully'})
    else:
        return jsonify({'message': 'user registration failed'})

@app.route('/auth/login', methods=['GET'])
def login_route():
    data = request.get_json()

    username = data['username']
    password = data['password']
    
    token = login.login_func(username, password)

    if token != False:
        return jsonify({'token': token, 'message': 'user logged in successfully'})
    else:
        return jsonify({'message': 'user login failed'})

@app.route('/auth/protected', methods=['GET'])
def authenticate():
    data = request.get_json()
    token = data['token']
    try:
        data = jwt.decode(token, key=token_secret, algorithms=['HS256', ])
        return jsonify({'message' : 'user authenticated successfully'})
    except:
        return jsonify({'message' : 'user authentication failed'})

if __name__ == '__main__':
    app.run(debug=True)