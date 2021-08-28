from flask import render_template, request
from . import indice

@indice.route("/")
def index():
    return render_template('index.html')

@indice.route("/calculo", methods=['POST'])
def direccion():
    address= request.form.get("address")
    return render_template('calculo.html', address=address)
