from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.dojos import Dojo 
from flask_app.models.ninja import Ninja 

# root
@app.route('/')
def index():
    return redirect('/dojos')

#Show dojos
@app.route('/dojos')
def all_users():
    return render_template('dojos.html', dojos = Dojo.get_all_dojos())


#Create a new dojo
@app.route('/dojos/create', methods=['post'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')

#Go to individual dojo. 
@app.route('/dojos/<int:id>')
def get_ninjas_in_dojos(id):
    dojos = Dojo.get_ninjas_and_dojos({ 'id': id })
    return render_template('show_dojos.html', dojos=dojos)


# @app.route('/users/<int:user_id>')
# def show(user_id):
#     user = User.show_single_user({'id': user_id})
#     return render_template('single_user.html', user=user)








