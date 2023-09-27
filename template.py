from flask import Flask, render_template, request
app = Flask(__name__)
a = "global name"
@app.route("/")
def mainp():
    # return("<h1>Hello main hai hm</h1>")
    return render_template("index.html")

@app.route("/login", methods = ['GET'])
def loginpage():
    username = request.args.get('uname')
    password = request.args.get('pass')    
    if username == "vivek" and password == "59":
        # return "<h1>WELCOME VIVEK</h1>"
        return render_template("index.html")
    else:
        return "<h2>WRONG USERNAME PASSWORD</h2>"
    # return render_template("login.html")

@app.route("/<uame>")
def namee(uame):
    usn = "vivek"
    return render_template("index.html", name = a )

@app.route("/m")
def m():
    nan = "4 cr per annum"
    return render_template("index.html", vv = nan)
app.run(debug = True)