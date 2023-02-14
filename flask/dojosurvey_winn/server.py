# Practice creating a server with Flask from scratch
# Practice adding routes to a Flask app
# Practice having the client send data to the server with a form
# Practice redirecting after the POST request.
# Use Session to display the form data on the result page.

# Build a new Flask application that accepts a form submission and presents the submitted data on a results page.

# The goal is to help you get familiar with sending POST requests through a form and displaying that information. Consider the below example as a guide.
# When you build this, please make sure that your program meets the following criteria:

# http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/process'
# Save form data into session.
# http://localhost:5000/result - have this display a html with the information that was submitted by POST
# Don't forget that any inputs we want to be able to access from the form submission need to have a name!

# It's always a good idea to print request.form to see if the form is delivering all the information you need in your routing method.

# __________________Worked with peyton________________
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Phish is good'

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/process', methods=['POST'])
def create_user():
    session['name'] = request.form['first_name']
    session['animal'] = request.form['animal']
    session['location'] = request.form['location']
    session['food'] = request.form['food']
    session['textbox'] = request.form['textbox']
    session['colorpick'] = request.form['colorpick']
    print(request.form)
    return redirect('/result')



@app.route('/result')
def obtain_user():
    
    return render_template('result.html')




if __name__ == "__main__":
    app.run(debug=True)
