from flask import Flask, render_template,session,request,redirect


app = Flask(__name__)
app.secret_key='boop'



@app.route("/")
def render_survey():
    if request.method =='POST':
        return redirect('submitted.html')
    else:
        return render_template("survey.html")


@app.route("/submitted.html", methods=['POST','GET'])
def render_submitted():
    
        session['name'] = request.form['name']
        return render_template('submitted.html')
        
    




if __name__=="__main__":
    app.run(debug=True)