from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():

    # Check if headers match expected values
    return 'Hello, World!'
    
if __name__ == '__main__':
    app.run()
