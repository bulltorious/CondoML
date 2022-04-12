from flask import Blueprint, render_template

from website import engine

views = Blueprint("views", __name__)
global engine

@views.route("/")
def index():

    return render_template("index.html")
    #return engine.file

@views.route("/lineargraphdata")
def lineargraphdata():
    #z = engine.dfarray()
    return str(engine.dfarray())

@views.route("/mvgraphdata")
def mvgraphdata():
    return str(engine.accuracy)