UNIVERSIDAD EVANGELICA DE EL SALVADOR
FACULTAD DE INGENIERÍA
MATERIA: SISTEMAS EXPERTOS
Estudiante: Christian Daniel Canizales Santos

Laborario registro numero 2.

Se debia generar un codigo a traves de las siguientes indicaciones.

1. Generar una estructura de datos que almacene 10 millones de puntos en una distribución
normal con una media de 500 y una escala de 30
2. Iterarla exclusivamente con estructuras de control
3. Calcular la sumatoria de los puntos que son menores a 500,000
4. Devolver el valor de la sumatoria y el tiempo en que la lógica de negocios del problema
tardo en ejecutarse

Se logro haciendo lo siguiente:

1. Se importo la libreria Numpy, a traves de esta creamos una vairable en la cual 
encapsulamos la creacion de numeros de naturaleza al azar. El nombre de esta variable se 
denomino como "al_azar", y la caracteristica utilizada fue "numpy.random.normal".
Tambien importamos la caracteristica "time" de python.
2. En el tema de las estructuras de control, la mas predominantemente utilizada en este
caso fue "for" con el cual asignariamos una accion a cada valor al azar dependiendo de 
si cumplian con una caracteristica cada uno. Asignamos una variable "inicio" para tomar
el tiempo de cuanto tardara nuestro aplicativo en realizar sus labores.
3.Dentro de nuestra estructura de control asignamos un "if" el cual lograra determinar 
si uno de los numeros al azar en el array posee la caracteristica de ser menor a 500,000
4.Utilizando "prints" imprimimos los resultados de la sumatoria en nuestro "for". Declaramos
un print para la variable "inicio" para que nos muestre el timepo en el que este se realizo

