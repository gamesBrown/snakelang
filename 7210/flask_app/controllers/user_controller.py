from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models.users import User
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)
@app.route("/")
def index():
    if "user_id" in session:
        del session["user_id"]
    return render_template("/login_reg.html")

@app.route("/success")
def render_success():
    if "user_id" in session:
        return render_template("/success.html")
    else:
        return redirect("/")
    

@app.route("/users/register", methods = ["POST"])
def register_user():
    print(request.form["email"])
    if not User.validate_user(request.form):
        print("Invalid User!")
        return redirect("/")
    else:
        print("Valid User!")
        pw_hash =bcrypt.generate_password_hash(request.form["password"])
        data = {
            "email":request.form["email"],
            "password":pw_hash
            
        }
        user_id = User.create_user(data)
        print(user_id)
        session["user_id"] = user_id
    return redirect("/success")

@app.route("/users/login", methods = ["POST"])
def email_login():
    data = {
        "email":request.form["email"]
        }
    print(User.login_with_email(data))
    user = User.login_with_email(data)
    if user==False:
        flash("Wrong Login Information, try again!")
        print("this code ran1")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Wrong Login Information, try again!")
        print("this code ran2")
        return render_template("/login_reg.html")

    print("this code ran3")
    session["user_id"] = user.idusers
    return redirect("/success")
@app.route("/logout",methods=["POST"])
def logout():
    
    if "user_id" in session:
        del session["user_id"]
    return redirect("/")


