from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route("/")
def hello():
    return "vivek kumar singh"

@app.route("/<na>/")
def printname(na):
    if na == "user":
        return redirect(url_for("j"))
    return "Hi there "+ na

@app.route("/m/<name>/")
def m(name):
    return "m is here "+name

@app.route("/<int:datee>")
def getd(datee):
    return "date = %d "%datee

@app.route("/<float:da>")
def getf(da):
    return "the float is %f"%da

@app.route("/j/<int:dba>")
def dbaa(dba):
    return "the dba is %d"%dba
app.run(debug = True)