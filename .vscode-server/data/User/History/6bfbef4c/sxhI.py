# app.py
from flask import Flask,request,render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

@app.route("/hello")
def hello():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}!"

@app.route("/greet", methods=["GET", "POST"]) 
def greet(): 
    if request.method == "POST":
        name = request.form.get("name", "Guest") 
        return f"Hello, {name}!" 
    return ''' 
	    <form method="post"> 
		Name: <input type="text" name="name"> 
		<input type="submit"> 
	    </form>
    '''
@app.route("/welcome/<name>")
def welcome(name):
    return render_template("index.html", name=name)


@app.route("/") 
def home(): return render_template("home.html") 
@app.route("/about") 
def about(): return render_template("about.html") 
@app.route("/submit", methods=["POST"]) 
def submit(): # 작업 처리 후 'Thank You' 페이지로 리다이렉트 
    return redirect(url_for("thank_you")) 
@app.route("/thank_you") 
def thank_you(): return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 15022, debug=True)
