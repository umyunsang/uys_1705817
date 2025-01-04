import json
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# 로그인 시에 저장된 회원정보를 불러오는 기능능
def load_users():
    return

# 회원 가입시에 회원 정보를 저장하는 기능능
def save_users(users):
    return

@app.route("/", methods=["GET", "POST"])
# 사용자가 입력한 이름과 아이디가 맞는지 확인
# 성공하면 세션에 저장하고 home으로 이동동
def login():
    message = None
    return render_template("login.html", message=message)

@app.route("/register", methods=["GET", "POST"])
# 사용자가 입력한 이름과 아이디를 저장장
def register():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        users = {}
        users[name] = password
        save_users(users)
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/home")
# 로그인하지 않은 사용자가 접근하면 로그인 페이지로 보냄
# 로그인에 성공하여 세션이 있으면 홈화면을 보여줌줌
def home():
    return render_template("home.html")

@app.route("/logout", methods=["POST"])
# 세션을 제거하고 로그인 화면으로 보냄냄
def logout():
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=15022)
