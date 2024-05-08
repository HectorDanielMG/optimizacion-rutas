import math
from flask import Flask, render_template

from HC.HCI import i_hill_climbing
from SA.SA import simulated_annealing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hill_climbing')
def hill_climbing():
    coord = {
        'Jiloyork': (19.916012, -99.580580),
        'Toluca': (19.289165, -99.655697),
        'Atlacomulco': (19.799520, -99.873844),
        'Guadalajara': (20.677754472859146, -103.34625354877137),
        'Monterrey': (25.69161110159454, -100.321838480256),
        'QuintanaRoo': (21.163111924844458, -86.80231502121464),
        'Michohacan': (19.701400113725654, -101.20829680213464),
        'Aguascalientes': (21.87641043660486, -102.26438663286967),
        'CDMX': (19.432713075976878, -99.13318344772986),
        'QRO': (20.59719437542255, -100.38667040246602)
    }

    ruta = i_hill_climbing(coord)
    distancia_total = evalua_ruta(ruta, coord)
    return render_template('index.html', hill_climbing_result={'ruta': ruta, 'distancia_total': distancia_total})

@app.route('/simulated_annealing')
def simulated_annealing_route():
    coord = {
        'Jiloyork': (19.916012, -99.580580),
        'Toluca': (19.289165, -99.655697),
        'Atlacomulco': (19.799520, -99.873844),
        'Guadalajara': (20.677754472859146, -103.34625354877137),
        'Monterrey': (25.69161110159454, -100.321838480256),
        'QuintanaRoo': (21.163111924844458, -86.80231502121464),
        'Michohacan': (19.701400113725654, -101.20829680213464),
        'Aguascalientes': (21.87641043660486, -102.26438663286967),
        'CDMX': (19.432713075976878, -99.13318344772986),
        'QRO': (20.59719437542255, -100.38667040246602)
    }

    ruta = simulated_annealing(coord)
    distancia_total = evalua_ruta(ruta, coord)
    return render_template('index.html', simulated_annealing_result={'ruta': ruta, 'distancia_total': distancia_total})

def evalua_ruta(ruta, coord):
    total = 0
    for i in range(len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    ciudad1 = ruta[-1]
    ciudad2 = ruta[0]
    total += distancia(coord[ciudad1], coord[ciudad2])
    return total

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

if __name__ == '__main__':
    app.run(debug=True)
