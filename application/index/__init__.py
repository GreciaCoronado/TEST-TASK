from flask import Blueprint


indice = Blueprint('index', __name__ ,template_folder='templates')

from . import routes