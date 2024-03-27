from tokenize import Double
from flask import Blueprint, render_template, request
from calc import Valueset, rcsolcalc, eulers

from decimal import *
getcontext().prec = 7

rc = Blueprint(__name__, "rc")

SolCord = []
EulersCord =[]
label = []
voltage = []
Eulersvoltage = []
@rc.route("/")
def rccalc():
    return render_template("rc.html", SolCord = SolCord, EulersCord = EulersCord, label = label, voltage = voltage, Eulersvoltage = Eulersvoltage)

@rc.route("/", methods = ['POST'])
def getvalue():
    global SolCord, EulersCord, label, voltage, Eulersvoltage
    Valueset(request.form['IVolt'], request.form['ResVal'], request.form['CapVal'], request.form['Maxtime'])
    SolCord = rcsolcalc() 
    EulersCord = eulers(request.form['Steptime'])
    label = [ row[0] for row in SolCord ]
    voltage = [ row[1] for row in SolCord ]
    Eulersvoltage = [ row[2] for row in EulersCord]
    return render_template('rc.html', SolCord = SolCord, EulersCord = EulersCord, label = label, voltage = voltage, Eulersvoltage = Eulersvoltage)
    

