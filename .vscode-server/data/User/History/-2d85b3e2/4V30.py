# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/hello")
def hello():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 15022, debug=True)
