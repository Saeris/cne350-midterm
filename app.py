# CNE350 Spring 2024 - RESTful DB Access
# Drake Costa <drake@saeris.io>
#
# A simple Flask app for serving a barebones HTML page
# with search and update forms, backed by a GET and POST
# request handler which reads and updates rows in a MariaDB
# database. Services managed via docker-compose.
#
# Adapted from: https://github.com/ellisju37073/States/blob/main/states/rest_web/rest_web.py

import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector
from flask import Flask, request, render_template
from flask_cors import CORS

db = mysql.connector.connect(
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_USER_PASSWORD'),
    database=os.getenv('MYSQL_DATABASE'),
    host=os.getenv('MYSQL_HOST'),
    port=int(os.getenv('MYSQL_PORT'))
)

cur = db.cursor()

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
   return render_template('index.html')

@app.route("/search", methods = ['GET'])
def searchStates():
    state = request.args.get('state')
    print(f"Recieved state: {state}")
    
    cur.execute("SELECT * FROM `states` WHERE State=%s", [state])
    result = cur.fetchall()
    stateFound = cur.rowcount == 1
    
    if stateFound:
        return f"Found state: {result[0][0]}, population: {result[0][1]}"
    else:
        return f"Unable to find state: {state}"

@app.route("/population", methods = ['POST'])
def updatePopulation():
    state = request.form['state']
    population = request.form['population']
    print(f"Recieved state: {state} and population: {population}")

    cur.execute("SELECT * FROM `states` WHERE State=%s", [state])
    cur.fetchall()
    stateFound = cur.rowcount == 1

    if stateFound:
        cur.execute("UPDATE `states` SET Population = %s WHERE State= %s;", [population, state])
        cur.execute("SELECT * FROM `states` WHERE State=%s and Population=%s", [state, population])
        cur.fetchall()
        stateUpdated = cur.rowcount == 1

        if stateUpdated:
            return f'Updated population for state: {state}'
        else:
            return f"Failed to update population for state: {state}"
    else:
        return f"Unable to find state: {state}"
        
if __name__ == '__main__':
    app.run()