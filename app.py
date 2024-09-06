from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace these with your actual token and private key values
EXPECTED_TOKEN = 'your_expected_token'
EXPECTED_PRIVATE_KEY = 'your_expected_private_key'

@app.route('/', methods=['GET'])
def hello_world():
    # Retrieve headers
    token = request.headers.get('token')
    private_key = request.headers.get('private-key')

    # Check if headers match expected values
    if token == EXPECTED_TOKEN and private_key == EXPECTED_PRIVATE_KEY:
        return 'Hello, World!'
    else:
        return jsonify({'error': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run()
