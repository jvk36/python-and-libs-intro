from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c0ef153ea0bf66a38af3"
    response = requests.get(blog_url).json()
    return render_template("blog-npoint-index.html", all_posts=response)


@app.route('/post/<num>')
def post(num):
    blog_url = "https://api.npoint.io/c0ef153ea0bf66a38af3"
    response = requests.get(blog_url).json()
    title = response[int(num)-1]["title"]
    subtitle = response[int(num)-1]["subtitle"]
    body = response[int(num)-1]["body"]
    return render_template("blog-npoint-post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
