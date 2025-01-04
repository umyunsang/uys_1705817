import json
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

def load_users():
    return

def save_users(users):
    return

@app.route("/", methods=["GET", "POST"])
def login():
    message = None
    return render_template("login.html", message=message)

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/logout", methods=["POST"])
def logout():
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=15022)
