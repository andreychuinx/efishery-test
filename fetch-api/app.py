import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Create some test data for our catalog in the form of a list of dictionaries.

@app.route('/', methods=['GET'])
def home():
    data = {
        'message': 'hello'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001)