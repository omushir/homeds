from flask import Flask, jsonify, request

app = Flask(__name__)

# Example endpoint
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')  # Get the 'name' parameter
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs on port 5000
