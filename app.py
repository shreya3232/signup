#from flask import Flask
from random import * 
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
#from app import app

app=Flask(__name__,template_folder="templates")
Bootstrap(app)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")
  
@app.route('/profile')
def profile():
    return render_template("profile.html")


if __name__=="__main__":
    app.run(debug=True)