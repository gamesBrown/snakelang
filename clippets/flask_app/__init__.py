from flask import Flask
from flask import render_template

app = Flask(__name__)
app.secret_key="Wow"

@app.route("/")
def renderHome():
    return render_template("testpage.html")
