from flask import Blueprint, redirect, render_template, request, flash, session, url_for
from flask_login import login_required, current_user
from sqlalchemy import func
from .models import Status, User, Caretaker
from . import db
from datetime import datetime

views = Blueprint("views", __name__)

@views.route("/")
def welcome():
    return render_template("welcome.html")

@views.route("/home", methods=["GET", "POST"])
@login_required
def home():
    data = request.form
    print(data)
    today = datetime.today().strftime('%m-%d-%Y')
    if request.method == "POST":
        date = request.form.get(str("my_hidden_input"))
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
        first_status = Status.query.filter_by(id=300).first()
        if date == "":
            flash("please enter the date", category="error")
        elif len(severity) < 1:
            flash("please enter the severity range", category="error")
        elif len(stress) < 1:
            flash("please enter the stress range", category="error")
        elif first_status is None:
            first_status = Status(
                id=300,
                date=date, 
                severity=severity, 
                stress=stress, 
                light=light, 
                sound=sound, 
                nausea=nausea, 
                aura=aura, 
                visual=visual, 
                dizzness=dizzness, 
                fatigue=fatigue, 
                unconcentrated=unconcentrated, 
                neck=neck, 
                user_id=current_user.id
            )
            db.session.add(first_status)
            db.session.commit()
            print("frist status created")
        else:
            new_status = Status(
                date=date, 
                severity=severity, 
                stress=stress, 
                light=light, 
                sound=sound, 
                nausea=nausea, 
                aura=aura, 
                visual=visual, 
                dizzness=dizzness, 
                fatigue=fatigue, 
                unconcentrated=unconcentrated, 
                neck=neck, 
                user_id=current_user.id
            )
            db.session.add(new_status)
            db.session.commit()
            flash("status updated", category="success")
    return render_template("home.html", user=current_user, today=today)

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
    information = User.query.filter_by(id=current_user.id).all()
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
    return render_template("profile.html", user=current_user, information=information)

@views.route("/care_home")
@login_required
def care_home():
    print(current_user)
    care_id = current_user.id
    print(care_id)
    user_card = (
        db.session.query(
            User.id, 
            User.name
        ).filter(
            User.caretaker_id == care_id
        ).all()
    )
    for i in user_card:
        print(i)
    return render_template("care_home.html", user=current_user, user_card=user_card)


@views.route("/care_update", methods=["GET", "POST"])
@login_required
def care_update():
    data = request.form
    print(data)
    if request.method == "POST":
        user_id = request.form.get("user_id")
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
            new_status = Status(
                user_id=user_id, 
                date=date, 
                severity=severity, 
                stress=stress, 
                light=light, 
                sound=sound, 
                nausea=nausea, 
                aura=aura, 
                visual=visual, 
                dizzness=dizzness, 
                fatigue=fatigue, 
                unconcentrated=unconcentrated, 
                neck=neck
            )
            db.session.add(new_status)
            db.session.commit()
            flash("status updated", category="success")
    return render_template("care_update.html", user=current_user)

@views.route("/care_profile", methods=["GET", "POST"])
@login_required
def care_profile():
    data = request.form
    print(data)
    print(int(current_user.id))
    if request.method == "POST":
        user_id = request.form.get("user_id")
        if len(user_id) < 1:
            flash("please enter the user id to add", category="error")
        elif not user_id:
            flash("Please enter the available user id to add", category="error")
        else:
            add_user = User.query.filter_by(id=user_id).first()
            if add_user:
                # Update the current user's caretaker relationship
                current_user.caretaker = Caretaker.query.get(current_user.id)
                current_user.caretaker.user.append(add_user)
                db.session.commit()
                flash(f"user {add_user.name} added successfully", category="success")
            else:
                flash("Invalid caretaker id, please try again", category="error")
    return render_template("care_profile.html", user=current_user)

@views.route("/user_details/<int:user_id>")
@login_required
def user_details(user_id):
    print(user_id)
    if user_id:
        status_details = (
            db.session.query(
                Status.id, 
                Status.date,
                Status.severity,
                Status.stress,
                Status.light,
                Status.sound,
                Status.nausea,
                Status.aura,
                Status.visual,
                Status.dizzness,
                Status.fatigue,
                Status.unconcentrated,
                Status.neck
            ).filter(
                Status.user_id == user_id
            ).all()
        )
        for i in status_details:
            print(i)
        return render_template("user_details.html", status_details=status_details)
    else:
        flash("User not found", "error")
        return redirect(url_for("views.care_home"))
    
@views.route("/admin_home")
@login_required
def admin_home():
    users = User.query.with_entities(User.id, User.name, User.email, User.caretaker_id, User.isActive).all()
    caretakers = Caretaker.query.with_entities(Caretaker.id, Caretaker.name, Caretaker.email, Caretaker.isActive).all()
    for i in users:
        print(f"User ID: {i.id}, Name: {i.name}, Email: {i.email}, Care: {i.caretaker_id}, isActive: {i.isActive}")
    for x in caretakers:
        print(f"Care ID: {x.id}, Name: {x.name}, Email: {x.email}, isActive: {x.isActive}")
    return render_template("admin_home.html", users=users, caretakers=caretakers)

@views.route("/edit_user/<int:user_id>", methods=["GET","POST"])
@login_required
def edit_user(user_id):
    print(user_id)
    data = request.form
    print(data)
    if request.method == "POST":
        user = User.query.get(user_id)
        new_email = request.form.get("new_email")
        new_name = request.form.get("new_name")
        new_caretaker_id = request.form.get("new_caretaker_id")
        if new_email is not None and new_email != "":
            user.email = new_email
        if new_name is not None and new_name != "":
            user.name = new_name
        if new_caretaker_id is not None and new_caretaker_id != "":
            user.caretaker_id = new_caretaker_id
        db.session.commit()
    return render_template("admin_edit_user.html")

@views.route("/de_active/<int:user_id>")
@login_required
def de_active(user_id):
    print(user_id)
    user = User.query.get(user_id)
    user.isActive = False
    db.session.commit()
    return redirect(url_for("views.admin_home"))

@views.route("/re_active/<int:user_id>")
@login_required
def re_active(user_id):
    print(user_id)
    user = User.query.get(user_id)
    user.isActive = True
    db.session.commit()
    return redirect(url_for("views.admin_home"))

@views.route("/edit_care/<int:care_id>", methods=["GET","POST"])
@login_required
def edit_care(care_id):
    print(care_id)
    data = request.form
    print(data)
    if request.method == "POST":
        caretaker = Caretaker.query.get(care_id)
        new_email = request.form.get("new_email")
        new_name = request.form.get("new_name")
        if new_email is not None and new_email != "":
            caretaker.email = new_email
        if new_name is not None and new_name != "":
            caretaker.name = new_name
        db.session.commit()
    return render_template("admin_edit_care.html")

@views.route("/de_active_care/<int:care_id>")
@login_required
def de_active_care(care_id):
    print(care_id)
    caretaker = Caretaker.query.get(care_id)
    caretaker.isActive = False
    db.session.commit()
    return redirect(url_for("views.admin_home"))

@views.route("/re_active_care/<int:care_id>")
@login_required
def re_active_care(care_id):
    print(care_id)
    caretaker = Caretaker.query.get(care_id)
    caretaker.isActive = True
    db.session.commit()
    return redirect(url_for("views.admin_home"))

@views.route("/status_details/<int:status_id>")
@login_required
def status_details(status_id):
    print(status_id)

