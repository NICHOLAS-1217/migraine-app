from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/")
def welcome():
    return render_template("welcome.html")

@views.route("/home")
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route("/migraineHistory")
@login_required
def migraine_history():
    return render_template("migraineHistory.html", user=current_user)

@views.route("/migraineResult")
@login_required
def migraine_result():
    return render_template("migraineResult.html", user=current_user)

@views.route("/contactUs")
@login_required
def contact_us():
    return render_template("contactUs.html", user=current_user)

@views.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@views.route("/care_home")
@login_required
def care_home():
    return render_template("care_home.html", user=current_user)
