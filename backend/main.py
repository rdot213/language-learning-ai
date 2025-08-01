from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the Language Learning AI backend!',
        'status': 'running'
    })

if __name__ == '__main__':
    app.run(debug=True)
