from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add CORS support to the Flask app

@app.route('/test')
def test():
    members = ["Member1", "Member2", "Member3"]
    return jsonify({"Members": members})

if __name__ == "__main__":
    app.run(debug=True)

