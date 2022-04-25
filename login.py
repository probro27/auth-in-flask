import jwt
import os
import connectionSQL as conn
from dotenv import load_dotenv
load_dotenv()

token_secret = os.getenv('TOKEN_SECRET')
pwd = os.getenv('password')

def login_func(username, password):
    connection = conn.create_server_connection("localhost", "root", pwd, "users")
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    cursor = connection.cursor()
    cursor.execute(query, values)
    result = cursor.fetchone()
    if result:
        token = jwt.encode({'username': username}, token_secret, algorithm='HS256')
        return token
    else:
        return False

