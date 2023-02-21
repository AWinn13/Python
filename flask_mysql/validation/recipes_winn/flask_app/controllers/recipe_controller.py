from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.loginandreg import User
from flask_app.models.recipes import Recipe


# -------------Dashboard-------------------
@app.route('/recipes')
def welcome_user():
    #!------Route Guard--------
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_id({'id': session['user_id']})
    all_recipes = Recipe.get_recipes_and_users()
    return render_template('welcome.html', user=user, all_recipes=all_recipes)

#------------Display Recipe--------
@app.route('/recipes/<int:id>')
def display_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_one_recipe({'id': id})
    user = User.get_id({'id': session['user_id']})
    return render_template('display_recipe.html', user=user, recipe=recipe)
    


# ------Render create template-------

@app.route('/recipes/create')
def render_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new_recipe.html')


# ------Submit New Recipe--------


@app.route('/recipes/create/new', methods=['post'])
def create_recipe():
    # Call the create_recipe method with the updated data and date
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/create')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Recipe.create_recipe(data)
    print('================',data)
    return redirect('/recipes')

#---------View recipe---------

@app.route('/recipes/<int:id>')
def view_recipe(name, user_id):
    if 'user_id' not in session:
        return redirect('/')
    recipes = Recipe.get_recipes_and_users({'name' : name, 'user_id': user_id })
    return render_template('display_recipe.html', recipes=recipes)

#-------Render Edit Recipe-------

@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    this_recipe = Recipe.get_one_recipe({'id': id})
    print('======================', this_recipe)
    return render_template('edit_recipe.html', this_recipe=this_recipe)

# ----------Update Recipe-----------------

@app.route('/recipes/<int:id>/update', methods=['post'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/{id}/edit')
    return redirect('/recipes')



#---------Delete Recipe--------
@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    Recipe.delete({'id': id})
    return redirect('/recipes')
