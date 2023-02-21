from flask import Flask, session
DB = 'recipes_schema'
app = Flask(__name__)
app.secret_key = "shhhhhh"
