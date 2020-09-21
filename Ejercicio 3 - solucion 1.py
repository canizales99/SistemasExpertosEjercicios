import time
import pandas as pd
import numpy as np

with open('costos.txt') as cost:
    costos = list(map(int, cost.read().split('\n')))

#opcion 1: utilizando un for iremos haciendo un append cada vez que el valor dentro sea menor o igual a 25

stopwatch =time.time()
gasto_tot = []
for producto in costos: 
    if producto <= 25:
        gasto_tot.append(producto)
print ('el negocio/tienda gastara: $',sum(gasto_tot), ' dolares')
print ('Duracion: {} segundos'.format(time.time() - stopwatch))

