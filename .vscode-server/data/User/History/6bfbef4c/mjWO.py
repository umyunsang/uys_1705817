import json
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret_key"

USER_FILE = "users.json"

def load_users():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file)

@app.route("/", methods=["GET", "POST"])
def login():
    message = None
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        users = load_users()
        if users.get(name) == password:
            session["user"] = name
            return redirect(url_for("home"))
        else:
            message = "Login Fail"
    return render_template("login.html", message=message)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        users = load_users()
        users[name] = password
        save_users(users)
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", user=session["user"])

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=15022)
