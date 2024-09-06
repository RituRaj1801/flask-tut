from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    response = {
        "status": 200,
        "message": "hello let be friend"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
