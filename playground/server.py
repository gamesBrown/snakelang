from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def render_index():
    return render_template("index.html")

@app.route("/row/<column_count>")
def render_playground():
    
    return render_template("play.html", box_count=box_count)
@app.route("/play/<int:box_count>/<string:back_color>")
def render_playground_change(box_count,back_color):
    return render_template("play.html", box_count=box_count,back_color=back_color)

if __name__=="__main__":
    app.run(debug=True)