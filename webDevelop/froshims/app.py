#Implements a registration form, storing registrants in a SQL db.


###-----------Dependencies----------###

from flask import Flask, redirect, render_template, request
import sqlite3

###-----------Global Declarations----------###

app = Flask (__name__)

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
    if not name or sport not in SPORTS:
        return render_template("failure.html")
    
    #Remember registrant
    db = sqlite3.connect("froshims.db")
    cur = db.cursor()
    cur.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", (name, sport) )
    db.commit()
    db.close()

    #Confirm registration
    return redirect("/registrants")

#Return Registrant List Logic
@app.route("/registrants")
def registrants():
    db = sqlite3.connect("froshims.db")
    cur = db.cursor()
    registrants = cur.execute("SELECT * FROM registrants").fetchall()
    return render_template("registrants.html", registrants=registrants)
    db.close()

#Deregister Registrant Logic
@app.route("/deregister", methods=["POST"])
def deregister():
    #Forget registrant
    id = request.form.get("id")
    if id:
        db = sqlite3.connect("froshims.db")
        cur = db.cursor()
        cur.execute("DELETE FROM registrants WHERE id =?", (id,)) #Need to implement security measures so only those with permisions can delete db items. Look into Flask's session variable
        db.commit()   
        db.close() 
    return redirect("/registrants")