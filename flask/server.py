from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes
    
@app.route('/dojo')
def dojo():
    return "dojo"
    
    # app.run(debug=True) should be the very last statement! 

@app.route('/say/flask')
def sayflask():
    return "Hi flask"

@app.route('/say/michael')
def saymichael():
    return "Hi michael"

@app.route('/say/john')
def sayjohn():
    return "Hi John"

@app.route('/say/flask')
def sayflask():
    return "flask"

@app.route('/say/repeat/35/hello')
def sayhello():
    for hello in range(36):
        print(f'hello')
    return ""
print(sayhello())

@app.route('/say/flask')
def sayflask():
    return "flask"





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


