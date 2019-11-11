from flask import Flask, jsonify
from flask_cors import CORS
from core import classify_user, calculate_level, update_users, is_user

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "Bank user classifier is running, use /users/<user id> \
        endpoint to classify unique bank user."


@app.route('/users/<user_id>')
def classify(user_id):
    classification = {}

    if is_user(user_id):
        classification["class"] = classify_user(user_id)
        classification["lvl"] = calculate_level(user_id)

    return jsonify(classification)

if __name__ == '__main__':
    update_users()
    app.run(debug=True)
