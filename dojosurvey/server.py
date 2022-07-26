from flask import Flask, render_template,session,request
import random # import the random module
random.randint(1, 100) 		# random number between 1-100




app = Flask(__name__)
app.secret_key = 'boop'

@app.route("/")
def render_index():
    session['answer']= random.randint(1,100)
    return render_template("index.html")

@app.route("/check", methods=['POST'])
def check_answer():
    session['input_number'] = int(request.form['input_number'])
    if session['input_number'] == session['answer']:
        message = "You Win"
        return render_template("victory.html",message=message)
    else:
        if session['input_number'] < session['answer']:
            message="Too Low!"
            return render_template("retry.html", message=message)
        else:    
            message="Too High!"
            return render_template("retry.html", message=message)



if __name__=="__main__":
    app.run(debug=True)