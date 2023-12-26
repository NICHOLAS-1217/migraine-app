from flask import Blueprint, render_template, request, flash

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
            flash("account created", category="success")
    return render_template("signup.html")