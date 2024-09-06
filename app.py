from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    response = {
        "status": 200,
        "message": "hello let be friend"
    }
    return jsonify(response)
@app.route('/about')
def about():
    response = {
        "status": 200,
        "message": "this is about component"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
