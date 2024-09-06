from flask import Flask, jsonify, request, render_template, redirect, url_for

# APPLICATION THAT PUBLISHES A BAREBONES REST API AND ALSO PROVIDE A WEB INTERFACE:
#
#  1. Publish routes for the REST API using Flask.
#  2. Publish other routes that uses the data to serve HTML pages.
#  3. Use Flask’s Jinja2 templating engine to dynamically generate HTML.
#  4. Handle form submissions using Flask to 
#
# Flask REST API Endpoints:
# 
# 1. GET /api/items: Returns all items as JSON.
# 2. GET /api/items/<int:item_id>: Returns a single item by its ID.
# 3. POST /api/items: Accepts a new item (via JSON) and adds it to the list.
#
# Flask Webpage Endpoints:
#
# 1. The root (/) serves a webpage that lists all items and includes a form to 
#    add a new item.
# 2. The form submission posts to /add_item, where Flask handles the form data 
#    and updates the list of items.
#
# Jinja2 Templates:
#
# 1. The index.html file uses Jinja2 to dynamically render the list of items 
#    and create a simple form.
# 2. The form posts to the /add_item endpoint, which will handle the addition 
#    of a new item and redirect back to the homepage.
#
# Running the Application:
#
# 1. The index.html file should be under the templates sub-directory.
# 2. Execute this file. 
# 3. Open browser and visit http://127.0.0.1:5000/.
#
# NOTE: Executes app.run(debug=True) when executing this file. This also means
# that code changes will automatically reload the application. This however
# will use the cached templates and such. To avoid, it stop the application
# and manually execute it again.
#
# HOW IT WORKS:
#
# 1. The home page (/) displays the list of items and provides a form to add 
#    new items.
# 2. When the form is submitted, the data is processed by adding it to the 
#    new list.
# 3. After adding the new item, the page is reloaded, and the updated list is 
#    displayed.
# 4. The API routes act similar to lib-flask-restapi.py except that the routes
#    are under /api/
#


app = Flask(__name__)

# Sample data (for the purpose of the example)
data = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
]

# API: GET all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data)

# API: GET a single item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 404

# API: POST a new item
@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.json
    new_item['id'] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201

# Web: Home page with the list of items and form to add a new item
@app.route('/')
def home():
    return render_template('index.html', items=data)

# Web: Handle form submission to add a new item
@app.route('/add_item', methods=['POST'])
def add_item_form():
    item_name = request.form['name']
    new_item = {'id': len(data) + 1, 'name': item_name}
    data.append(new_item)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
