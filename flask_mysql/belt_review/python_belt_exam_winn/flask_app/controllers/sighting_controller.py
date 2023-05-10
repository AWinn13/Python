from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.loginandreg import User
from flask_app.models.sighting import Sighting


# -------------Dashboard-------------------
@app.route("/sightings")
def welcome_user():
    #!------Route Guard--------
    if "user_id" not in session:
        return redirect("/")
    user = User.get_id({"id": session["user_id"]})
    return render_template("welcome.html", user=user, all_sightings = Sighting.get_all() )


# ------------Display sighting--------
@app.route("/sightings/<int:id>")
def display_sighting(id):
    if "user_id" not in session:
        return redirect("/")
    sighting = Sighting.get_one_sighting({"id": id})
    user = User.get_id({"id": session["user_id"]})
    all_sightings = Sighting.get_all()
    return render_template("display_sighting.html", user=user, sighting=sighting )


# ------Render create template-------


@app.route("/sightings/create")
def render_sighting():
    if "user_id" not in session:
        return redirect("/")
    return render_template("new_sighting.html")


# ------Submit New sighting--------


@app.route("/sightings/create/new", methods=["post"])
def create_sighting():
    if "user_id" not in session:
        return redirect("/")
    if not Sighting.validate_sighting(request.form):
        return redirect("/sightings/create")
    data = {**request.form, "user_id": session["user_id"]}
    Sighting.create_sighting(data)
    return redirect("/sightings")


# ---------View sighting---------


# @app.route("/sightings/<int:id>")
# def view_sighting(name, user_id):
#     if "user_id" not in session:
#         return redirect("/")
#     sightings = Sighting.get_sightings_and_users({"name": name, "user_id": user_id})
#     return render_template("display_sighting.html", sightings=sightings)


# -------Render Edit sighting-------


@app.route("/sightings/<int:id>/edit")
def edit_sighting(id):
    if "user_id" not in session:
        return redirect("/")
    this_sighting = Sighting.get_one_sighting({"id": id})
    return render_template("edit_sighting.html", this_sighting=this_sighting)


# ----------Update sighting-----------------


@app.route("/sightings/<int:id>/update", methods=["post"])
def update_sighting(id):
    if "user_id" not in session:
        return redirect("/")
    if not Sighting.validate_sighting(request.form):
        return redirect("/sightings/create")
    data = {**request.form, "user_id": session["user_id"], 'id':id}
    Sighting.update_sighting(data)
    return redirect("/sightings")


# ---------Delete sighting--------
@app.route("/sightings/<int:id>/delete")
def delete_sighting(id):
    if "user_id" not in session:
        return redirect("/")
    Sighting.delete_sighting({"id": id})
    return redirect("/sightings")

@app.route("/sightings/<int:id>/skeptic", methods=["post"])
def update_skeptic(id):
    if "user_id" not in session:
        return redirect("/")
    data = {**request.form, "user_id": session["user_id"], 'id':id}
    Sighting.update_skeptic(data)
    return redirect("/sightings")
