from flask import Flask

# CHECKOUT OFFICIAL TUTORIAL: https://flask.palletsprojects.com/en/3.0.x/tutorial/

# BAREBONES APPLICATION EXAMPLE

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/') and bind it to the hello function
@app.route('/')
def hello():
    return "Hello, World!"

# Run the Flask app on the local server
if __name__ == '__main__':
    app.run(debug=True)
