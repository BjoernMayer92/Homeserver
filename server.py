from flask import Flask
import sqlite3
import sys,os
from database import connect_to_database


app = Flask(__name__)

@app.route("/")

def hello_world():
	return "<p>Hello World<\p>"



if __name__ == "__main__":
	path = os.path.join(".","database.db")
	conn = connect_to_database(path)
	app.run(debug=True, host = "0.0.0.0", port = 5000)	


