from flask import Flask, render_template

app = Flask(__name__)

# Define a route that accepts a name variable
@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html', name=name)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
