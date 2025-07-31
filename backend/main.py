# main.py - Prometheus Language AI Backend Starter

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Prometheus Language AI Backend is running!",
        "status": "online",
        "version": "0.1"
    })

if __name__ == "__main__":
    app.run(debug=True)
