from flask import Flask
from .index import indice


miApp= Flask(__name__)
miApp.config.from_pyfile('config/configuration.cfg')
miApp.register_blueprint(indice)



