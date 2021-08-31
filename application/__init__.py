from flask import Flask
from .index import index


miApp= Flask(__name__)
miApp.config.from_pyfile('config/configuration.cfg')
miApp.register_blueprint(index)



