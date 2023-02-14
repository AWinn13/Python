from flask import Flask, render_template  
app = Flask(__name__)    

@app.route('/play')          
def play1():
    render_template('index.html')
    return render_template('index.html')



# @app.route('/play/<int:num>')          
# def play2(num):
#     return render_template('index.html')


# @app.route('/play/<int:num>/<string:color>')          
# def play3():
#     return render_template('index.html')


if __name__=="__main__":   
    app.run(debug=True) 