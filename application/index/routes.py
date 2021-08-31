import requests
import math
from flask import render_template, request
from . import index
from .data import mkad_km

#GET METHOD
@index.route("/")
def home():
    return render_template('index.html')

#POST METHOD
@index.route("/distanceToMKAD", methods = ['POST'])
def distance():
    
    address = request.form.get("address")

    '''Transform the address into coordinate using the Yandex Geocode API'''
    API_KEY = 'WRITE YOUR API KEY'
    url = 'https://geocode-maps.yandex.ru/1.x'
    params = dict(apikey=API_KEY, geocode= address , format='json')

    res = requests.get(url, params = params)
    json = res.json()
    coordinate = json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    coordinate = coordinate.split()

    '''Calculates the distance between the coordinate of the given address and the coordinates within the MKAD.
    Returns the smallest distance value in km, which correspond to the closest point of the MKAD.
    If the specified address is located inside the MKAD it isn't calculated.
    '''
    lat1 = float(coordinate[1])
    lon1 = float(coordinate[0])
    km_ = []
    for i in mkad_km:
        if lat1 == i[2] and lon1 == i[1] :
            km = 0
            break
        else:
            lat2 = i[2]
            lon2 = i[1]
            rad = math.pi/180
            dlat = lat2-lat1
            dlon = lon2-lon1
            R = 6372.795477598
            a = (math.sin(rad*dlat/2))**2 
            + math.cos(rad*lat1) * math.cos(rad*lat2) * (math.sin(rad*dlon/2))**2
            distance_km = 2 * R * math.asin(math.sqrt(a))
            km_.append(distance_km)
            km = min(km_) 
             
    return render_template('distance.html', km = km, address = address)



