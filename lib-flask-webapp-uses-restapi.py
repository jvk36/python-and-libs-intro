from flask import Flask, render_template, request, redirect, url_for
import requests

# WEB APPLICATION THAT USES THE REST API PUBLISHED BY lib-flask-restapi.py on port 5000:
#
# 1. The web application will call the API published by lib-flask-restapi.py 
#    to fetch and add items.
# 2. It uses Python’s requests library to send HTTP requests to the API
#
# NOTE: JavaScript Fetch API may be used instead of Python/Flask to interact 
# with API endpoints, but we are just sticking with Python.
#
# FINAL STRUCTURE:
# 
# 1. API: lib-flask-restapi.py running on port 5000 provides GET and POST 
#     endpoints (/items).
# 2. Web Application: lib-flask-webapp-uses-restapi.py (this file) running
#     on port 5001 makes HTTP requests to the API to display and add items
#     using the requests library.
#
# REST API Interaction:
#
# 1. requests.get: The web app calls the API (GET /api/items) to fetch the 
#    list of items, which are then passed to the HTML template.
# 2. requests.post: When the form is submitted, the web app sends a POST 
#    request with the new item data to the API (POST /api/items). If the 
#    item is successfully added, the page is refreshed with the updated list.
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
# 1. Ensure the API (from the original Flask API code) is running 
#    on http://127.0.0.1:5000/
# 2. Execute this file. 
# 3. Open browser and visit http://127.0.0.1:5001/.
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
# 2. When the form is submitted, the data is sent via a POST request to the 
#    /add_item route, which processes the form data and adds a new item to the 
#    list.
# 3. After adding the new item, the page is reloaded, and the updated list is 
#    displayed.
#


app = Flask(__name__)

# Point the web app to the API running on port 5000
API_URL = 'http://127.0.0.1:5000/items'

@app.route('/')
def home():
    response = requests.get(API_URL)
    items = response.json() if response.status_code == 200 else []
    
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['POST'])
def add_item_form():
    item_name = request.form['name']
    new_item = {'name': item_name}
    response = requests.post(API_URL, json=new_item)
    
    if response.status_code == 201:
        return redirect(url_for('home'))
    else:
        return "Error: Could not add item", 400

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Web app runs on port 5001
