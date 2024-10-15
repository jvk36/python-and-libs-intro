from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


# including a variable in the route
@app.route('/username/<name>')
def greeting(name):
    return f"<h1 style='text-align: center'>Hello {name}</h1><p>This is a paragraph.</p>"


# including a variable name with "path" as type specification
@app.route('/<path:name>')
def greeting_with_path(name):
    return f"Hello {name}"


# including a variable name with an integer type specification
@app.route('/echo_number/<int:number>')
def echo_message(number):
    return str(number)


# multiple variables
@app.route('/<username>/<int:age>')
def echo_name_and_age(username, age):
    return f"My name is {username} and I am {age} years old"


if __name__ == "__main__":
    app.run(debug=True)
