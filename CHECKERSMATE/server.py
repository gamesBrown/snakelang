from tkinter.tix import ButtonBox
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def return_index():
    return render_template("index.html")
@app.route("/<string:boxColor>/<string:boxColor2>/cols<int:column_count>/rows<int:row_count>")
def render_playground(column_count,boxColor,boxColor2,row_count):
    
        return render_template("index.html",column_count=column_count,boxColor=boxColor,boxColor2=boxColor2,row_count=row_count)

if __name__=="__main__":
    app.run(debug=True)