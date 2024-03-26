from tokenize import Double
from flask import Blueprint, render_template, request
from calc import Valueset, rcsolcalc, eulers
rc = Blueprint(__name__, "rc")

@rc.route("/")
def rccalc():
    return render_template("rc.html")

@rc.route("/", methods = ['POST'])
def getvalue():
    Valueset(request.form['IVolt'], request.form['ResVal'], request.form['CapVal'], request.form['Maxtime'])
    SolCord = rcsolcalc() 
    EulersCord = eulers(request.form['Steptime'])
    return render_template('rc.html', SolCord = SolCord, EulersCord = EulersCord)
    

