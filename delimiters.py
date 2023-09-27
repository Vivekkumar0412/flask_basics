from  flask import Flask, render_template
app = Flask(__name__)
global_name = "VIVEK SINGH RAJPUT"
arr = [20,30,40,90]
dict = {"maths":99, "computer":90, "english":98}
@app.route("/")
def main():
    return render_template("values.html", global_naam = global_name)
@app.route("/<name>")
def n(name):
    return render_template("values.html", naam = name)

@app.route("/<int:int_val>")
def initt(int_val):
    return render_template("values.html", int_html_val = int_val)
@app.route("/j")
def jj():
    return render_template("values.html", arr_data = arr, dict_val = dict)
app.run(debug = True)