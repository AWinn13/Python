# __________________Worked with peyton________________ 
from flask import Flask, render_template, redirect, session  
app = Flask(__name__)    
app.secret_key = 'Phish'

@app.route('/')
def counter():
    if not 'visit' in session:
        session['visit'] = 1
    else:
        session['visit'] += 1
    return render_template('index.html')

@app.route('/plustwo')
def counter():
    if not 'visit' in session:
        session['visit'] = 1
    else:
        session['visit'] += 2
    return render_template('index.html')

    
# adding this method
@app.route('/backtoone')
def start_over():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True) 