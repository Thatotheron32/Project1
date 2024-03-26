from tokenize import Double
from flask import Blueprint, render_template, request
from calc import Valueset, rcsolcalc, eulers
rc = Blueprint(__name__, "rc")

@rc.route("/")
def rccalc():
    return render_template("rc.html")

@rc.route("/", methods = ['POST','GET'])
def getvalue():
    Valueset(request.form.get['IVolt'], request.form.get['ResVal'], request.form.get['CapVal'], request.form.get['Maxtime'])
    SolCord = rcsolcalc() 
    EulersCord = eulers(request.form.get['Steptime'])
    return render_template('rc.html', SolCord = SolCord, EulersCord = EulersCord)
    

