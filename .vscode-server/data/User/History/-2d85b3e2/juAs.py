# app.py
from flask import flask

app = flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 15022, debug=True)
    