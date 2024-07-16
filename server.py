from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    data = request.get_json()
    print(data)
    return 'Success', 200

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(port=5000)