# app.py
from flask import Flask,request,render_template

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 15022, debug=True)
