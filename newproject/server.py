from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def sundae_form():
    return render_template("form.html")

@app.route("/sundaes/submit", methods=["POST"])
def submit_sundae():
    print(request.form['name'])
    return render_template("display.html")

if __name__ == "__main__":
    app.run(debug=True)