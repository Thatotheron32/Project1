from flask import Blueprint,  render_template

home = Blueprint(__name__, "home")

@home.route("/")
def hometep():
    return render_template("home.html")

