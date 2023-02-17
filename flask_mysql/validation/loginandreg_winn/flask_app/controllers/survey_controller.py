from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.surveys import Survey


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey', methods=['post'])
def create_dojo():
    if not Survey.validate_survey(request.form):
        return redirect('/')
    
    Survey.create(request.form)
    return redirect('/result')


@app.route('/result')
def fill_survey():
    return render_template('result.html', survey = Survey.get_survey() )







