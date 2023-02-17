from flask import Flask, session
DB = 'dojosurvey_schema'
app = Flask(__name__)
app.secret_key = "shhhhhh"
