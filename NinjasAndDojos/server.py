from flask_app import app
from flask import render_template

from flask_app.models.ninja import Ninja



@app.route("/")
def renderHome():
    Ninja.get_ninjas()
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)

