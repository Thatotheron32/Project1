from flask import Blueprint,  render_template

project = Blueprint(__name__, "project")

@project.route("/")
def home():
    return render_template("index.html")

