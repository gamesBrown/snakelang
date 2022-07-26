from flask_app import app
from flask import render_template,redirect,session,request


from flask_app.models.dojo import Dojo



@app.route("/single_dojo")
def render_single_dojo():
    
    return "single dojo"

@app.route("/dojo_view")
def render_dojos():
    all_dojos = Dojo.get_dojos()
    
    return render_template("dojo_view.html", all_dojos=all_dojos)


@app.route("/create_dojo" ,methods=["POST"])
def create_dojos():
        data = {
            "name": request.form["name"]

            }
        Dojo.dojo_create(data)

    
        return redirect("dojo_created.html")



@app.route("/dojo_created")
def dojo_created():
    
    return render_template("dojo_created.html")


@app.route("/dojo_form")
def dojo_form():
    
    return render_template("dojo_form.html")






