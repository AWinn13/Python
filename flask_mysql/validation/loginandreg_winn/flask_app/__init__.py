from flask import Flask, session
DB = 'loginreg_schema'
app = Flask(__name__)
app.secret_key = "shhhhhh"
