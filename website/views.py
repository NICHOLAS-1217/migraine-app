from flask import Blueprint, render_template, request, flash, session
from flask_login import login_required, current_user
from sqlalchemy import func
from .models import Status, User, Caretaker
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
    if request.method == "POST":
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
    status = Status.query.filter_by(user_id=current_user.id).all()
    return render_template("migraineHistory.html", user=current_user, status=status)

@views.route("/migraineResult")
@login_required
def migraine_result():
    avg_severity = db.session.query(func.avg(Status.severity).label('average_severity')).filter_by(user_id=current_user.id).scalar() or 0
    avg_stress = db.session.query(func.avg(Status.stress).label('average_stress')).filter_by(user_id=current_user.id).scalar() or 0
    return render_template("migraineResult.html", user=current_user, avg_severity=avg_severity, avg_stress=avg_stress)

@views.route("/contactUs")
@login_required
def contact_us():
    return render_template("contactUs.html", user=current_user)

@views.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    data = request.form
    print(data)
    if request.method == "POST":
        care_id = request.form.get("care_id")
        if len(care_id) < 1:
            flash("please enter the caretaker email to confirm", category="error")
        else:
            confirmed_care = Caretaker.query.filter_by(id=care_id).first()
            if confirmed_care:
                # Update the current user's caretaker relationship
                current_user.caretaker = confirmed_care
                db.session.commit()
                flash(f"Caretaker {confirmed_care.name} confirmed successfully", category="success")
            else:
                flash("Invalid caretaker id, please try again", category="error")
    return render_template("profile.html", user=current_user)

@views.route("/care_home")
@login_required
def care_home():
    return render_template("care_home.html", user=current_user)
