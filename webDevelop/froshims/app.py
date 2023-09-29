from flask import Flask, render_template, request

app = Flask (__name__)

REGISTRANTS = {} #Declares an empty dictionary. Also, all caps because you cannot have a variable and a function have the same name.
#coding convention is to use all caps for global variables.

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("failure.html")
    sport = request.form.get("sport")
    if sport not in SPORTS:
        return render_template("failure.html")
    REGISTRANTS[name] = sport #enters a sport value for the name key (key:value pair)
    return render_template("success.html")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)