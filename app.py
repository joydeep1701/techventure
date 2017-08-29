from sql import *
from helpers import *
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
import time
from werkzeug.datastructures import ImmutableMultiDict
import json

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response
# custom filter
#app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///tv.db")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/comingsoon")
def csoon():
    flash("TLDR:Not Ready","warning")
    return render_template("comsoon.html")

@app.route("/login",methods=["GET","POST"])
def login():
    """ Logs User In"""

    session.clear() #clear any previous user id
    if request.method == "POST":
        if not request.form.get("roll"):
            flash('must provide username','danger')
            return render_template("login.html")
        elif not request.form.get("password"):
            flash('must provide password','danger')
            return render_template("login.html")
        else:
            rows = db.execute("""SELECT * FROM users WHERE UnivRoll = :roll""",
            roll=html_escape(request.form.get("roll")))
            if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["Password"]):
                flash('Invalid password', 'danger')
                return render_template("login.html")
            session["uroll"] = rows[0]["UnivRoll"]
            session["name"] = rows[0]["Name"]

            return redirect(url_for("index"))
    else:
        flash("TLDR:Not Ready","warning")
        return render_template("login.html")
@app.route("/register",methods=["GET","POST"])
def register():
    session.clear() #remove old username
    if request.method == "POST":
        if not request.form.get("roll"):
            flash("must provide university roll","danger")
            return render_template("login.html")
        elif not request.form.get("password1"):
        	flash('must provide password', 'danger')
        	return render_template("login.html")
        elif not request.form.get("name"):
        	flash('must provide name', 'danger')
        	return render_template("login.html")
        rows = db.execute("SELECT * FROM users WHERE UnivRoll = :roll",roll=html_escape(request.form.get("roll")))
        if len(rows) != 0:
            flash("Roll No Used","danger")
        db.execute("INSERT INTO 'users' ('Name','Stream','UnivRoll','Password') VALUES (:name,:stream,:uroll,:password)",name=html_escape(request.form.get("name")),stream=html_escape(request.form.get("stream")),uroll=html_escape(request.form.get("roll")),password = pwd_context.hash(request.form.get("password1")))
        session["uroll"] = request.form.get("roll")
        session["name"] = request.form.get("name")
        return redirect(url_for("index"))
@app.route("/checkuserid/<ui>", methods=["GET"])
def checkuserid(ui):
    """Checks UserID during login"""
    rows = db.execute("SELECT * FROM users WHERE UnivRoll = :roll",roll=html_escape(ui))
    return str(len(rows))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
