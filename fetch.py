from flask import Flask, jsonify
import database

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    conn = database.create_connection()
    users = database.get_users(conn)
    database.close_connection(conn)
    return jsonify(users)