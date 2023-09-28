from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def main():
    return "main page is here"

@app.route("/student")
def st():
    return "STUDENTS ARE HERE"

@app.route("/user/<name>")
def user(name):
    if name == "student":
        return redirect(url_for('student'))
    # return "hi"


app.run(debug = True)