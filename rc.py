from flask import Blueprint, render_template

rc = Blueprint(__name__, "rc")

@rc.route("/")
def rccalc():
    return render_template("rc.html")