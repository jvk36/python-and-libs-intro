from flask import Flask, jsonify, request

# APPLICATION THAT PUBLISHES A BAREBONES REST API:
# 
# EXPLANATION:
#
# Flask Setup:
#
# 1. We import Flask, jsonify, and request.
# 2. The app = Flask(__name__) initializes a Flask application.
#
# Basic Endpoints:
# 
# 1. GET /items: Returns a list of items in JSON format.
# 2. GET /items/<item_id>: Fetches a single item by its ID.
# 3. POST /items: Accepts a JSON payload to add a new item.
#
# Running the Application:
#
# Execute this file and the REST API will be accessible 
# at http://127.0.0.1:5000/.

# EXAMPLE REQUESTS:
#
# 1. GET all items: 
#       curl http://127.0.0.1:5000/items
# 2. GET an item by ID: 
#       curl http://127.0.0.1:5000/items/1
# 3. POST to create a new item: 
#   Linux/bash/etc.:
#       curl -X POST -H "Content-Type: application/json" -d '{"name": "New Item"}' http://127.0.0.1:5000/items
#   PowerShell (windows):
#       Invoke-RestMethod -Uri http://127.0.0.1:5000/items -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{"name": "New Item"}'
#       OR
#       Invoke-WebRequest -Uri http://127.0.0.1:5000/items -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"name": "New Item"}'
#
# NOTE: curl command is aliased to Invoke-RestMethod but there can be problems with nested quotes and so the Invoke- commands are better. 


app = Flask(__name__)

# Sample data (for the purpose of the example)
data = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask REST API!"

# GET request to fetch all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# GET request to fetch a single item by its id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 404

# POST request to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    new_item['id'] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)

