from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import datetime

app = Flask(__name__)

# mysql configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3310         #if not entered, db cant access
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cucci'        #db cucci laundry app
mysql = MySQL(app)

# USERS ENDPOINT
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users")
        column_names = [i[0] for i in cursor.description]
        
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(column_names, row)))
        
        # Close connection and return data
        cursor.close()
        return jsonify(data)
    
    elif request.method == 'POST':
        # Get data from request 
        username = request.json['username']
        role = request.json['role']
        email = request.json['email']
        password = request.json['password']

        # Connect to database and execute SQL statement
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO USERS (username, role, email, password) VALUES (%s, %s, %s, %s)"
        val = (username, role, email, password)
        cursor.execute(sql, val)

        # Commit changes and close connection
        mysql.connection.commit()
        cursor.close()

        # Return success message
        return jsonify({'message': 'Data Added Successfully!'})

        
@app.route('/detailusers', methods=['GET'])
def detailusers():
    if 'id' in request.args:
        cursor = mysql.connection.cursor()
        id = request.args.get('id')
        sql = "SELECT * FROM users WHERE id = %s"
        val = (id,)
        cursor.execute(sql,val)

        column_names = [i[0] for i in cursor.description]
        
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(column_names, row)))
        
        # Close connection and return data
        cursor.close()
        return jsonify(data)
    
@app.route('/deleteusers', methods=['DELETE'])
def deleteusers():
    # Get id parameter from request
    id = request.args.get('id')
    cursor = mysql.connection.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)

    # Commit changes and close connection
    mysql.connection.commit()
    cursor.close()

    # Return success message
    return jsonify({'message': 'Data Deleted Successfully!'})

@app.route('/editusers', methods=['PUT'])
def editusers():
    if 'id' in request.args:
        data = request.get_json()
        cursor = mysql.connection.cursor()
        sql = "UPDATE users SET username = %s, role= %s, email=%s, password=%s WHERE id = %s"
        val = (data['username'], data['role'], data['email'], data['password'], request.args['id'], )
        cursor.execute(sql, val)

        # Commit changes and close connection
        mysql.connection.commit()
        cursor.close()

        # Return success message
        return jsonify({'message': 'Data Updated Successfully!'})


# ORDERS ENDPOINT
@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM orders")
        column_names = [i[0] for i in cursor.description]
        
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(column_names, row)))
        
        # Close connection and return data
        cursor.close()
        return jsonify(data)
    
    elif request.method == 'POST':
        # Get data from request
        custName = request.json['custName']
        ordCat = request.json['ordCat']
        ordDate = datetime.datetime.now()
        progress = request.json['progress']
        status = request.json['status']
        payment = request.json['payment']

        # Connect to database and execute SQL statement
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO orders (custName, ordCat, ordDate, progress, status, payment) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (custName, ordCat, ordDate, progress, status, payment)
        cursor.execute(sql, val)

        # Commit changes and close connection
        mysql.connection.commit()
        cursor.close()

        # Return success message
        return jsonify({'message': 'Data Added Successfully!'})

@app.route('/deleteorders', methods=['DELETE'])
def deleteorders():
    # Get id parameter from request
    id = request.args.get('orderID')
    cursor = mysql.connection.cursor()
    
    # Delete by ID
    del_id = "DELETE FROM orders WHERE `orders`.`orderID` = %s"
    val = (id,)
    cursor.execute(del_id, val)

    # Delete by custName
    del_name = "DELETE FROM orders WHERE `orders`.`custName` = %s"
    val = (request.args.get('custName'),)
    cursor.execute(del_name, val)

    # Commit changes and close connection
    mysql.connection.commit()
    cursor.close()

    # Return success message
    return jsonify({'message': 'Data Deleted Successfully!'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=90, debug=True)