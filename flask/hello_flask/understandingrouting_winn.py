from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


    
@app.route('/say/dojo')
def dojo():
    return "dojo"
    

@app.route('/say/flask')
def sayflask():
    return "Hi flask"

@app.route('/say/michael')
def saymichael():
    return "Hi michael"

@app.route('/say/john')
def sayjohn():
    return "Hi John"


@app.route('/say/repeat/<int:num>/<string:hello>')
def sayhello(num, hello):
    result = ''
    for i in range(num):
        result += 
    return f'<p>{hello}<p>'*num






if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


