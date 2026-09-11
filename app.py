import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "AI DevOps Demo",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/health/live")
def health_live():
    return jsonify({
        "status": "alive"
    })


@app.route("/health/ready")
def health_ready():
    return jsonify({
        "status": "ready"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
