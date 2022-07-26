from flask_app import app
from flask import render_template,redirect,session,request



@app.route("/add_hero.html" ,methods = ["POST","GET"])
def add_hero():
    if request.method==["GET"]:
        return render_template("add_hero.html")
    if request.method==["POST"]:
        return redirect("/")