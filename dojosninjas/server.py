from flask import render_template
from flask_app import app
from flask_app.controllers import dojo_controller,ninja_controller




@app.route("/")
def index():
    return render_template("landing.html")






if __name__ == "__main__":
    app.run(debug=True)