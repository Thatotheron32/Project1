#imports both the flask library and the project blueprint
from flask import Flask, redirect, url_for
from project import project
from rc import rc
app = Flask(__name__)

@app.route("/")
def go_to_home():
    return redirect(url_for("project.home"))

app.register_blueprint(project, url_prefix= "/home")
app.register_blueprint(rc, url_prefix= "/home/rcclac")

if __name__ == 'main':
    app.run(debug=True, port=5000)