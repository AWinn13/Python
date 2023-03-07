from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.users import User



@app.route('/')
def index():
    return redirect('/users')

#Shows all users
@app.route('/users')
def all_users():
    return render_template('show_user.html', users = User.get_all())

# Adds a new user 
@app.route('/users/new')
def new_user():
    User.save(request.form)
    return render_template('index.html')

## Redirects to the newly completed user 
@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


#Diplays a single users profile
@app.route('/users/<int:user_id>')
def show(user_id):
    user = User.show_single_user({'id': user_id})
    return render_template('single_user.html', user=user)

# Renders an auto-filled form, to edit the user
@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    user = User.show_single_user({'id': user_id})
    return render_template('edit_user.html',user=user)


# Updates user in database 
@app.route('/users/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')


# Delete user from db 
@app.route('/users/<int:user_id>/delete')
def delete(user_id):
    User.delete(user_id)
    return redirect('/')