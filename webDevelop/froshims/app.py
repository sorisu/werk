#Implements a registration form, storing registrants in a SQL db.


###-----------Dependencies----------###

from flask import Flask, render_template, request #need to import flask module.
from tbd import SQL #need to import SQL module.

###-----------Global Declarations----------###

app = Flask (__name__)

db = SQL("") #enter the path to the SQL db

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

###-----------Juicy Part of the Web App----------###

#Default Landing Page Logic
@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


#Register Registrant Logic 
@app.route("/register", methods=["POST"])
def register():
    #Validate submission
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or sport in SPORTS:
        return render_template("failure.html")
    
    #Remember registrant
    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)

    #Confirm registration
    return redirect("/registrants")

#Return Registrant List Logic
@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)

#Deregister Registrant Logic
@app.route("/deregister", methods=["POST"])
def deregister():
    #Forget registrant
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id =?, id") #Need to implement security measures so only those with permisions can delete db items. Look into Flask's session variable
    return redirect("/registrants")