from flask import Flask

from website import mlengine

engine = mlengine.mlengine(file='condos_march_2022.csv')
engine.multivariate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"


    from .views import views


    app.register_blueprint(views, url_prefix="/")


    return app
