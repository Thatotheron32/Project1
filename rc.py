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
    Valueset(Double(request.form['IVolt']),Double(request.form['ResVal']),Double(request.form['CapVal']),Double(request.form['Maxtime']))
    CalcV = rccalc()
    Voltage,dvdx,x,deltaY,steps =  eulers(Double(request.form['Steptime']))
    return render_template('rc.html')
    

