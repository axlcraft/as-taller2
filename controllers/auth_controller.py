from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.user import User
from extensions import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Registro de usuarios
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        db_session = db.SessionLocal()
        if db_session.query(User).filter_by(username=username).first():
            flash("El nombre de usuario ya está en uso", "danger")
            return redirect(url_for("auth.register"))

        user = User(username=username, email=email)
        user.set_password(password)
        db.add(user)
        db.commit()

        flash("Registro exitoso, ahora puedes iniciar sesión", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


# Inicio de sesión
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db_session = db.SessionLocal()
        user = db.query(User).filter_by(username=username).first()

        if user and user.check_password(password):
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Sesión iniciada correctamente", "success")
            return redirect(url_for("index"))

        flash("Credenciales inválidas", "danger")

    return render_template("login.html")


# Cerrar sesión
@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Has cerrado sesión", "info")
    return redirect(url_for("auth.login"))
