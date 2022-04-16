from flask import Flask, request, render_template, redirect
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))

myapp=Flask(__name__,template_folder='templates')

@myapp.route("/")
def homepage():
    return render_template("index.html")

@myapp.route("/", methods = ["POST"])
def checklogin():
    UN = request.form['Username']
    PW = request.form['Password']

    sqlconnection = sqlite3.Connection(currentlocation + "\Login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT Username, Password From Users WHERE Username = '{un}' AND Password = '{pw}'".format(un = UN, pw = PW)

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) == 1:
        return render_template("LoggedIn.html")
    else:
        return redirect("/register")

@myapp.route("/register", methods = ["GET", "POST"])
def registerpage():
    if request.method == "POST":
       dUN = request.form['DUsername']
       dPW = request.form['Dpassword']
       Uemail = request.form['EmalUser']
       sqlconnection = sqlite3.Connection(currentlocation + "\Login.db")
       cursor = sqlconnection.cursor()
       query1 = "INSERT INTO Users VALUES('{u}', '{p}', '{e}')".format(u = dUN, p = dPW, e = Uemail)
       cursor.execute(query1)
       sqlconnection.commit()
       return redirect("/")
    return render_template("register.html")
    

    
if __name__ == '__main__':
    myapp.run()