from flask import render_template
from flask_app import app
from flask import render_template

@app.route("/")
def renderHome():
    return render_template("testpage.html")


if __name__=="__main__":
    app.run(debug=True)


