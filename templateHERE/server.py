from flask import Flask, render_template,session


app = Flask(__name__)

@app.route("/<int:count>")
def render_index(count):
    return render_template("index.html",count=count)

if __name__=="__main__":
    app.run(debug=True)