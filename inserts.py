from flask import Flask, request, jsonify
import database

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    
    conn = database.create_connection()
    database.add_user(conn, name, email)
    database.close_connection(conn)
    
    return jsonify({'message': 'User added successfully'}), 201

if __name__ == '__main__':
    app.run(port=5000)