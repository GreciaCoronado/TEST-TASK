from flask import render_template, request
from flask.templating import DispatchingJinjaLoader
from . import indice
from .db import mkad_km
import requests
import math

@indice.route("/")
def index():
    return render_template('index.html')


@indice.route("/calculo", methods=['POST'])

def coordenada():
    address= request.form.get("address")

    API_KEY = '52b98c38-dba8-4d11-b63b-268b1d8ff66a'
    url = 'https://geocode-maps.yandex.ru/1.x'
    params = dict(apikey=API_KEY, geocode= address , format='json')

    res = requests.get(url, params=params)
    json = res.json()
    point= json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    point= point.split()

    lat1=float(point[1])
    lat2=55.774558
    lon1=float(point[0])
    lon2=37.842762

    for i in mkad_km:
        if lat1 == i[2] :
            distancia=0
            break
        else:
            print(lat1,lat2)
            rad=math.pi/180
            dlat=lat2-lat1
            dlon=lon2-lon1
            R=6372.795477598
            a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
            distancia=2*R*math.asin(math.sqrt(a))

    return render_template('calculo.html', distancia=distancia)



