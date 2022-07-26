from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models.dojo import Dojo

from flask_app.models.ninja import Ninja



@app.route("/ninja_view")
def render_ninja():
    all_ninjas = Ninja.get_ninjas()
    all_dojos = Dojo.get_dojos()
    
    return render_template("ninja_view.html", all_ninjas=all_ninjas, all_dojos=all_dojos)


@app.route("/ninja_form")
def ninja_form():
    
    return render_template("ninja_form.html")



@app.route("/create_ninja",methods=["POST"])
def create_ninja():
        data = {
            "username": request.form["username"],
            "password": request.form["password"],
            "email": request.form["email"]


            }
        Ninja.create_ninja(data)

    
        return redirect("ninja_created.html")

@app.route("/ninja_created.html")
def ninja_created():
    
    return render_template("ninja_created.html")


