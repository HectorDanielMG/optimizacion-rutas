import math
import random

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

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

def simulated_annealing(coord, temperatura_inicial=1000, factor_enfriamiento=0.99, iteraciones_por_temp=100):
    ruta_actual = list(coord.keys())
    mejor_ruta = ruta_actual[:]
    temperatura = temperatura_inicial
    
    while temperatura > 1:
        for _ in range(iteraciones_por_temp):
            ciudad1, ciudad2 = random.sample(ruta_actual, 2)
            indice1, indice2 = ruta_actual.index(ciudad1), ruta_actual.index(ciudad2)
            ruta_nueva = ruta_actual[:]
            ruta_nueva[indice1], ruta_nueva[indice2] = ruta_nueva[indice2], ruta_nueva[indice1]
            costo_actual = evalua_ruta(ruta_actual, coord)
            costo_nuevo = evalua_ruta(ruta_nueva, coord)
            delta_costo = costo_nuevo - costo_actual
            
            if delta_costo < 0 or random.random() < math.exp(-delta_costo / temperatura):
                ruta_actual = ruta_nueva[:]
                if evalua_ruta(ruta_actual, coord) < evalua_ruta(mejor_ruta, coord):
                    mejor_ruta = ruta_actual[:]
        
        temperatura *= factor_enfriamiento
    
    return mejor_ruta

if __name__ == "__main__":
    coord = {
        'Jiloyork' :(19.916012, -99.580580),
        'Toluca':(19.289165, -99.655697),
        'Atlacomulco':(19.799520, -99.873844),
        'Guadalajara':(20.677754472859146, -103.34625354877137),
        'Monterrey':(25.69161110159454, -100.321838480256),
        'QuintanaRoo':(21.163111924844458, -86.80231502121464),
        'Michohacan':(19.701400113725654, -101.20829680213464),
        'Aguascalientes':(21.87641043660486, -102.26438663286967),
        'CDMX':(19.432713075976878, -99.13318344772986),
        'QRO':(20.59719437542255, -100.38667040246602)
    }
    
    mejor_ruta = simulated_annealing(coord)
    print("Ruta óptima:", mejor_ruta)
    print("Distancia Total:", evalua_ruta(mejor_ruta, coord))
