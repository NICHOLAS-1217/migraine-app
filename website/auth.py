from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["get", "post"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "logout"

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    data = request.form
    print(data)
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        if len(email) < 4:
            flash("email must be greater than 3 characters", category="error")
        elif len(name) < 2:
            flash("name must be greater than 1 characters", category="error")
        elif len(password) < 7:
            flash("password dont\'t match", category="error")
        elif password != confirmPassword:
            flash("password too short", category="error")
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("account created", category="success")
            return redirect(url_for("views.home"))

    return render_template("signup.html")