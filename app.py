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
def search():
    zipcode = request.args.get('zipcode')
    print(f"Recieved zipcode: {zipcode}")
    
    cur.execute("SELECT * FROM `zipcodes` WHERE Zipcode=%s", [zipcode])
    result = cur.fetchall()
    
    if cur.rowcount == 1:
        return f"Found zipcode: {result[0][0]}, population: {result[0][1]}"
    else:
        return f"Unable to find zipcode: {zipcode}"

@app.route("/update", methods = ['POST'])
def update():
    zipcode = request.form['zipcode']
    population = request.form['population']
    print(f"Recieved zipcode: {zipcode} and population: {population}")

    cur.execute("SELECT * FROM `zipcodes` WHERE Zipcode=%s", [zipcode])
    cur.fetchall()

    if cur.rowcount == 1:
        cur.execute("UPDATE `zipcodes` SET Population = %s WHERE Zipcode= %s;", [population, zipcode])
        cur.execute("SELECT * FROM `zipcodes` WHERE Zipcode=%s and Population=%s", [zipcode, population])
        cur.fetchall()

        if cur.rowcount == 1:
            return f'Updated population for zipcode: {zipcode}'
        else:
            return f"Failed to update population for zipcode: {zipcode}"
    else:
        return f"Unable to find zipcode: {zipcode}"
        
if __name__ == '__main__':
    app.run()