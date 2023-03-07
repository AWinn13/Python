from flask import Flask, session
DB = 'books'
app = Flask(__name__)
app.secret_key = "shhhhhh"
