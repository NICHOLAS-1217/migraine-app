from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Caretaker
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["get", "post"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("logged in succesfully", category="success")
                login_user(user)
                return redirect(url_for("views.home"))
            else:
                flash("incorrect password, try again", category="error")
        else:
            flash("email dose not exist", category="error")
    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    data = request.form
    print(data)
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        user = User.query.filter_by(email=email).first()
        if user:
            flash("email already exists", category="error")
        elif len(email) < 4:
            flash("email must be greater than 3 characters", category="error")
        elif len(name) < 2:
            flash("name must be greater than 1 characters", category="error")
        elif len(password) < 7:
            flash("password dont\'t match", category="error")
        elif password != confirmPassword:
            flash("password not same", category="error")
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash("account created", category="success")
            return redirect(url_for("views.home"))
    return render_template("signup.html")

@auth.route("/care_login", methods=["get", "post"])
def care_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        caretaker = Caretaker.query.filter_by(email=email).first()
        if caretaker:
            if check_password_hash(caretaker.password, password):
                flash("logged in succesfully", category="success")
                login_user(caretaker)
                return redirect(url_for("views.care_home"))
            else:
                flash("incorrect password, try again", category="error")
        else:
            flash("email dose not exist", category="error")
    return render_template("care_login.html")

@auth.route("/care_signup", methods=["GET", "POST"])
def care_signup():
    data = request.form
    print(data)
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        caretaker = Caretaker.query.filter_by(email=email).first()
        if caretaker:
            flash("email already exists", category="error")
        elif len(email) < 4:
            flash("email must be greater than 3 characters", category="error")
        elif len(name) < 2:
            flash("name must be greater than 1 characters", category="error")
        elif len(password) < 7:
            flash("password dont\'t match", category="error")
        elif password != confirmPassword:
            flash("password too short", category="error")
        else:
            new_caretaker = Caretaker(email=email, name=name, password=generate_password_hash(password, method="sha256"))
            db.session.add(new_caretaker)
            db.session.commit()
            login_user(new_caretaker)
            flash("account created", category="success")
            return redirect(url_for("views.care_home"))
    return render_template("care_signup.html")