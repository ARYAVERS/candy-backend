import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/get-color", methods=["GET"])
def get_color():
    return jsonify({"color": "#2ecc71"})


if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host=host, port=port)
