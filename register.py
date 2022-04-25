import jwt
import connectionSQL as conn
import os
from dotenv import load_dotenv
load_dotenv()
token_secret = os.getenv('TOKEN_SECRET')
pwd = os.getenv('password')

def register_func(username, password):
    connection = conn.create_server_connection("localhost", "root", pwd, "users")
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = (username, password)
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    token = jwt.encode({'username': username}, token_secret, algorithm='HS256')
    return token

