from flask import Flask, render_template,request,redirect
from sqlalchemy import create_engine
DataBase_Engine=create_engine("postgresql://postgres:admin@localhost/postgres")
import pandas as pd
import psycopg2
import numpy


conn=psycopg2.connect(
    database="postgres",
    user='postgres',
    password='admin'
)
# conn.autocomit=True
cursor=conn.cursor()



app = Flask(__name__)

@app.route("/")
def home():
    return """<iframe
    allow="microphone;"
    width="350"
    height="430"
    src="https://console.dialogflow.com/api-client/demo/embedded/30214714-1003-42c0-8a07-3bdefed57ef4">
</iframe>
"""
    # return render_template("home.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        username = req.get("username")
        email = req["email"]
        password = request.form["password"]

        # You could also use 
        password = request.form.get("password")
        insert_query="insert into dm_marts.flask_data values('{}','{}','{}')".format(username,email,password)
        print(insert_query)
        # pd.read_sql(insert_query,con=DataBase_Engine)
        cursor.execute(insert_query)
        conn.commit()
        conn.close()

        return 'success'

    return render_template("sign_up.html")


if __name__ == "__main__":
    app.run(debug=True)
