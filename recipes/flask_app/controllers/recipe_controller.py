
from flask_app import app
from flask import render_template, session, redirect,request
from flask_app.models.users import User
from flask_app.models.recipes import Recipe
from flask import flash


@app.route("/")
def index():
    
    user_list = User.get_users()
    return render_template("index.html",user_list=user_list)
@app.route("/create_recipe")
def create_recipe():
    if session["user_id"]:
        data = {
            "id":session["user_id"]
        }
    else:
        redirect("/")
    logged_user = User.get_one_user_by_id(data)

    



    return render_template("/create_recipe.html",user=logged_user)

@app.route("/edit_recipe/<int:id>")
def edit_recipe(id):

    data = {
        "id":id
    }
    recipe = Recipe.display_recipe_with_poster(data)
    data = {
        "id":session["user_id"]
    }
    session["id"] = recipe.id

    user = User.get_one_user_by_id(data)


    if user.id != recipe.poster.id:
        flash("you didn't make that recipe!")
        return redirect("/dashboard")
    if recipe.under30 ==1:
        recipe.under30 = "on"

    



    return render_template("/edit_recipe.html", user=user,recipe=recipe)

@app.route("/post_recipe", methods=["POST"])
def post_recipe():

    
    recipe ={
        "name":request.form["name"],
        "description":request.form["description"],
        "instructions":request.form["instructions"],
        "under30":0,
        "user_id":session["user_id"]

    }
    if "under30" in request.form:
        recipe["under30"]=1

    Recipe.create_recipe(recipe)
    
    

    print(recipe)

    return redirect("/dashboard")
@app.route("/post_edit", methods=["POST"])
def post_edit():

    recipe ={
        "id":session["id"],
        "name":request.form["name"],
        "description":request.form["description"],
        "instructions":request.form["instructions"],
        "under30":0,
        
        

    }
    if "under30" in request.form:
        recipe["under30"]=1
    flashRedirect = False
    if recipe["name"] == "" or recipe["name"] == None:
        flash("Please enter a name")
        flashRedirect = True
    if recipe["description"] == "" or recipe["description"] == None:
        flash("Please enter a value for your description")
        flashRedirect = True
    if recipe["instructions"] == "" or recipe["instructions"] == None:
        flash("Please enter a value for your instructions")
        flashRedirect = True
   
    if flashRedirect == True:
        return redirect("/edit_recipe/" +str(recipe["id"]))


   
    Recipe.edit_recipe(recipe)
    del session["id"]
    

    return redirect("/dashboard")
@app.route("/delete_recipe/<int:id>")
def delete_recipe(id):
    data={
        "id":id
    }
    recipe = Recipe.display_recipe_with_poster(data)
    if session["user_id"] != recipe.poster.id:
        flash("you didn't make that recipe!")
        return redirect("/dashboard")
    else:
        data = {
            "id": recipe.id
        }
        Recipe.del_recipe(data)
        return redirect("/dashboard")

@app.route("/view_recipe/<int:id>")
def view_recipe(id):
    data = {
        "id":id
            }

    print(Recipe.display_recipe_with_poster(data))
    recipe = Recipe.display_recipe_with_poster(data)

    
    data = {
        "id":session["user_id"]
    }
    logged_user = User.get_one_user_by_id(data)




    return render_template("/view_recipe.html",id=id,user=logged_user,recipe=recipe)



@app.route("/dashboard")
def dashboard_view():
    if "user_id" not in session:
        flash("Please login before you try and view recipes! :D")
        return redirect("/")
    else:
        data = {
            "id":session["user_id"]
        }
        logged_user = User.get_one_user_by_id(data)
 
        

    
    

    
    recipe_list = Recipe.get_recipes()

    return render_template("dashboard.html",recipe_list = recipe_list,user=logged_user )

@app.route("/logout",methods=["POST"])
def logout():
    if session["user_id"]:
        del session["user_id"]

    return redirect("/")