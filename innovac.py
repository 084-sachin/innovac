from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.secret_key = 'super secret key'
db = SQLAlchemy(app)


class innovac(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Roll = db.Column(db.String(9),unique=True)
    password = db.Column(db.String(100))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/event")
def event():
    return render_template("event.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/event/mind_matrix")
def ctf():
    return render_template("ctf.html")

@app.route("/event/mothra")
def mothra():
    return render_template("mothra.html")

@app.route("/event/marathon")
def marathon():
    return render_template("marathon.html")

@app.route("/event/reverse")
def reverse():
    return render_template("reverse.html")

@app.route("/event/nerdiness")
def dicey():
    return render_template("dicey.html")


@app.route("/register",methods=["POST", "GET"])
def register():
    if request.method=="POST":  
        name = request.form["name"]
        roll = request.form["roll"]
        password = request.form["password"]
        user = innovac(Name=name, Roll=roll, password=password)
        db.session.add(user)
        db.session.commit()
        return render_template("login.html")
    return render_template("register.html") 

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        Roll = request.form["RollNo"]
        password = request.form["password"]
        user = innovac.query.filter_by(Roll = Roll).first()
        if user:
            if password == user.password:
                return redirect(url_for('index'))
            else:
                return render_template("login.html",error="Incorrect Password")
        else:
            return render_template("login.html",error="You are not registered")
    else:
        return render_template("login.html")