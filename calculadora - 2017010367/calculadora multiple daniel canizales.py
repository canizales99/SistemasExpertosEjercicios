#importamos librerias como math y tkinter.
from tkinter import *
from tkinter import ttk
import math

#ABRIMOS LA VENTANA DE TKINTER
calculadora=Tk()
calculadora.title("calculadora multiple - Daniel Canizales")
#calculadora.wm_iconbitmap('calcutron.ico')
entrada=Entry(calculadora, width=50) #aqui añadimos una textbox
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



#DEFINIMOS LAS ACCIONES DE CADA UNO DE LOS BOTONES:

#el numero representado en la pantalla
def anadirboton(number):
    actual= entrada.get()
    entrada.delete(0,END)
    entrada.insert(0, str(actual) + str(number)) #con esto evitamos que los numeros aparezcan desordenados

#accion de borrado de lo que hay en el textbox a traves del boton "borrar"
def borrar():
    entrada.delete(0,END)

def suma():
    primer_numero=entrada.get()
    # llamamos variables globales para que se puedan usar en todo el proyecto
    global num1
    global operacion
    operacion="suma"
    num1 = float(primer_numero)
    entrada.delete(0,END)

def resta():
    primer_numero=entrada.get()
    global num1
    global operacion
    operacion="resta"
    num1 = int(primer_numero)
    entrada.delete(0,END)

def multiplicacion():
    primer_numero=entrada.get()
    global num1
    global operacion
    operacion="multiplicacion"
    num1 = int(primer_numero)
    entrada.delete(0,END)

def division():
    primer_numero=entrada.get()
    global num1
    global operacion
    operacion="division"
    num1 = int(primer_numero)
    entrada.delete(0,END)

def raiz():
    primer_numero=entrada.get()
    global num1
    global operacion
    num1 = float(primer_numero)
    entrada.delete(0, END)
    entrada.insert(0, math.sqrt (float(num1)))

def exponente():
    primer_numero=entrada.get()
    global num1
    global operacion
    operacion = "exponente"
    num1 = int(primer_numero)
    entrada.delete(0,END)


#LLEGAMOS AL BOTON IGUAL.
#utilizamos el if para diferenciar cuando sea cada una de las operaciones a excepcion de la raiz.
def igual():
    num2 = entrada.get()
    entrada.delete(0,END)
    if operacion == "suma":
        entrada.insert(0, num1 + int(num2))
    if operacion == "resta":
        entrada.insert(0, num1 - int(num2))
    if operacion == "multiplicacion":
        entrada.insert(0, num1 * int(num2))
    if operacion == "division":
        entrada.insert(0, num1 / int(num2))
    if operacion == "exponente":
        entrada.insert(0, num1 ** int(num2))


#definimos los botones numericos de la calculadora
#utilizamos el "lambda" para lograr capturar un valor de cada uno de los botones
boton1= Button(calculadora, text="1", padx=40, pady=40, command=lambda: anadirboton(1))
boton2= Button(calculadora, text="2", padx=40, pady=40, command=lambda: anadirboton(2))
boton3= Button(calculadora, text="3", padx=40, pady=40, command=lambda: anadirboton(3))
boton4= Button(calculadora, text="4", padx=40, pady=40, command=lambda: anadirboton(4))
boton5= Button(calculadora, text="5", padx=40, pady=40, command=lambda: anadirboton(5))
boton6= Button(calculadora, text="6", padx=40, pady=40, command=lambda: anadirboton(6))
boton7= Button(calculadora, text="7", padx=40, pady=40, command=lambda: anadirboton(7))
boton8= Button(calculadora, text="8", padx=40, pady=40, command=lambda: anadirboton(8))
boton9= Button(calculadora, text="9", padx=40, pady=40, command=lambda: anadirboton(9))
boton0= Button(calculadora, text="0", padx=40, pady=40, command=lambda: anadirboton(0))

#definimos los botones de operaciones basicas
botonsuma= Button(calculadora, text="+", padx=40, pady=40, command=suma)
botonresta= Button(calculadora, text="-", padx=40, pady=40, command=resta)
botonmultiplicacion= Button(calculadora, text="*", padx=40, pady=40, command=multiplicacion)
botondivision= Button(calculadora, text="/", padx=40, pady=40, command=division)

#definimos los botones de las operaciones mas complejas
botonexponente= Button(calculadora, text="^", padx=40, pady=40, command=exponente)
botonraiz= Button(calculadora, text="sqrt", padx=40, pady=40, command=raiz)

#botones "igual" y "borrado"
botonigual= Button(calculadora, text="=", padx=40, pady=40, command=igual)
botonborrar= Button(calculadora, text="borrar", padx=40, pady=40, command=borrar)

#poner los numeros en la pantalla a traves de una cuadrilla o "grid"
boton0.grid(row=4, column=0)
boton1.grid(row=3, column=0)
boton2.grid(row=3, column=1)
boton3.grid(row=3, column=2)
boton4.grid(row=2, column=0)
boton5.grid(row=2, column=1)
boton6.grid(row=2, column=2)
boton7.grid(row=1, column=0)
boton8.grid(row=1, column=1)
boton9.grid(row=1, column=2)

botonsuma.grid(row=3, column=3)
botonresta.grid(row=3, column=4)
botondivision.grid(row=1, column=3)

botonmultiplicacion.grid(row=1, column=4)
botonexponente.grid(row=2, column=3)
botonraiz.grid(row=2, column=4, columnspan=2)

botonigual.grid(row=4, column=3, )
botonborrar.grid(row=4, column=4, columnspan=2)




calculadora.mainloop()
