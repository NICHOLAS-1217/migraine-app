from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Status
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def welcome():
    return render_template("welcome.html")

@views.route("/home", methods=["GET", "POST"])
@login_required
def home():
    data = request.form
    print(data)
    if request.method =="POST":
        date = request.form.get("datepicker")
        severity = request.form.get("severity")
        stress = request.form.get("stress")
        light = request.form.get("light")
        sound = request.form.get("sound")
        nausea = request.form.get("nausea")
        aura = request.form.get("aura")
        visual = request.form.get("visual")
        dizzness = request.form.get("dizzness")
        fatigue = request.form.get("fatigue")
        unconcentrated = request.form.get("unconcentrated")
        neck = request.form.get("neck")
        if len(date) < 1:
            flash("please enter the date", category="error")
        elif len(severity) < 1:
            flash("please enter the severity range", category="error")
        elif len(stress) < 1:
            flash("please enter the stress range", category="error")
        else:
            new_status = Status(date=date, severity=severity, stress=stress, light=light, sound=sound, nausea=nausea, aura=aura, visual=visual, dizzness=dizzness, fatigue=fatigue, unconcentrated=unconcentrated, neck=neck, user_id=current_user.id)
            db.session.add(new_status)
            db.session.commit()
            flash("status updated", category="success")
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
