import jwt
import connectionSQL as conn

def register_func(username, password):
    connection = conn.create_server_connection("localhost", "root", "prabhav1234!@#", "users")
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = (username, password)
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    token = jwt.encode({'username': username}, 'secret', algorithm='HS256')
    return token

