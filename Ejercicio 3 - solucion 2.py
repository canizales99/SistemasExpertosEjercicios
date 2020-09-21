import time
import pandas as pd
import numpy as np

#opcion numero 2: cargamos el txt a traves de 'loadtxt', esto nos facilita manejar los valores dentro. 
precios = np.loadtxt('costos.txt')

stopwatch = time.time()
costomenos = np.sum(precios[precios <= 25])
print('el negocio/tienda gastara: $', costomenos, ' dolares')
print('Duracion: {} segundos'.format(time.time() - stopwatch))
