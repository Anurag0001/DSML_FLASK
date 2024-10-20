from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/")
def main_page():
    return "<p>Welcome to my Website!</p>"