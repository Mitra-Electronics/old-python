from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the main page <h1>HELLO<h1>"

@app.route("/<name>")
def user(name):
    return "<h1>Error 404</h1>"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/Sanjay Mitra")
def Sanjay():
    return "Hi Sanjay <h1>How are you<h1>"

if __name__ == "__main__":
    app.run()
