from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'test_db'

mysql = MySQL(app)

# Define API routes
@app.route('/users', methods=['GET'])
def get_users():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    data = cursor.fetchone()
    cursor.close()
    if data:
        return jsonify(data)
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (user['name'], user['email']))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'User created successfully'})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = request.get_json()
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (user['name'], user['email'], user_id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
