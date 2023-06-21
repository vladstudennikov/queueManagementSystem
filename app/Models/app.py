from flask import Flask, render_template, Response, request, session, redirect, jsonify
from flask_session import Session
from LoginController import LoginController
from Admin import Admin
from Operator import Operator
from Workplace import Workplace
from Monitor import Monitor
from QueueServices import QueueService
from BusinessLogic import BusinessLogic
import json


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SECRET_KEY'] = 'f54dY6edHkusf25f55If2Qe'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


""""variables"""
logic = BusinessLogic()


@app.route('/operator/<int:number>')
def operator(number):
    global logic

    if request.method == "GET":
        """if session["username"] != "operator" or session["userid"] != number:
            return render_template("errorscreen.html", error_name = "Access denied", error_message = "You do not have access to this page")"""

        operator = logic.getWorkplaceOperator(number)

        return render_template(
            "operator.html", 
            id=number,
            name=operator.name,
            surname=operator.surname,
            state=logic.getWorkplaceById(number).getstate())


@app.route('/admin/<int:number>', methods=["GET", "POST"])
def admin(number):
    if request.method == "GET":
        """if session["username"] != "admin" or session["userid"] != number:
            return render_template("errorscreen.html", error_name = "Access denied", error_message = "You do not have access to this page")"""

        return render_template('admin.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    global logic

    if request.method == "GET":
        return render_template("login.html")
    else:
        login = request.form.get("username")
        pwd = request.form.get("password")

        if login == "":
            return render_template("errorscreen.html", error_name = "No login", error_message = "Please, enter login")
        if pwd == "":
            return render_template("errorscreen.html", error_name = "No password", error_message = "Please, enter password")
        
        try:
            user = logic.getUserByLogin(login, pwd)
        except:
            return render_template("errorscreen.html", error_name = "User was not found", error_message = "User was not found. Check login and password")

        if type(user) is Operator:
            session["username"] = "operator"
            session["userid"] = user.id
            return redirect("/operator/" + str(user.id))
        if type(user) is Monitor:
            session["username"] = "monitor"
            session["userid"] = user.id
            return redirect("/monitor/" + str(user.id))
        if type(user) is Admin:
            session["username"] = "admin"
            session["userid"] = user.id
            return redirect("/admin/" + str(user.id))


@app.route('/monitor/<int:number>')
def monitor(number):
    if request.method == "GET":
        """if session["username"] != "monitor" or session["userid"] != number:
            return render_template("errorscreen.html", error_name = "Access denied", error_message = "You do not have access to this page")"""

        return render_template("monitor.html")
    

def customersJson():
    global logic
    l = {"data": [i.id for i in logic.getCustomers()]}
    return jsonify(l)


def workplacesJson():
    global logic 
    l = logic.getWorkplaces()
    res = dict()

    for key, value in l.items():
        if value is not None:
            res[key.id] = value.id

    return jsonify(res)


def workplaceStatesJson():
    global logic
    l = logic.getWorkplaces().keys()
    print(l)

    res = dict()
    for i in l:
        res[f"Operator {i.id}"] = i.getstate()
    return jsonify(res)


@app.route('/addCustomer', methods=["POST"])
def addCustomer():
    global logic
    if request.method == "POST":
        logic.addCustomer()
        return customersJson()
    

@app.route('/getCustomers', methods=["POST"])
def getCustomers(): 
    if request.method == "POST":
        return customersJson()
    

@app.route('/getWorkplaces', methods=["POST"])
def getWorkplaces(): 
    if request.method == "POST":
        return workplacesJson()
    

@app.route('/setState', methods=["GET"])
def setState():
    global logic
    if request.method == "GET":
        id = request.args.get('id')
        state = request.args.get('status')
        logic.changeWorkplaceState(
            workplace=int(id),
            state=state
        )
        
        return jsonify("success", 204)
    

@app.route('/getStates', methods=["GET"])
def getStates():
    global logic
    if request.method == "GET":
        return workplaceStatesJson()


if __name__ == '__main__':
    #type in brackets "host=<private ipv4 adress of the computer in LAN>" 
    #to make this app work in all computers of LAN
    app.run()