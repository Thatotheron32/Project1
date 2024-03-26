from tokenize import Double
from flask import Blueprint, render_template, request
from calc import Valueset, rccalc, eulers
rc = Blueprint(__name__, "rc")

@rc.route("/")
def rccalc():
    x = 0
    CalcV = 0
    return render_template("rc.html")

@rc.route("/", methods = ['POST'])
def getvalue():
    Valueset(request.form['IVolt'], request.form['ResVal'], request.form['CapVal'], request.form['Maxtime'])
    CalcV = [0,1,2,3,4,5,6,7,8,9]
    x = [0,1,2,3,4,5,6,7,8,9]
    return render_template('rc.html', CalcV = CalcV, x=x,)
    

