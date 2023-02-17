from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja 
from flask_app.models.dojos import Dojo 


#Show dojos
@app.route('/ninja')
def new_ninja():
    return render_template('new_ninja.html', dojos=Dojo.get_all_dojos())


#Create a new dojo
@app.route('/ninja/create', methods=['post'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect("/dojos")

# Adds a new user 
# @app.route('/users/new')
# def new_ninja():
#     User.save(request.form)
#     return render_template('index.html')

