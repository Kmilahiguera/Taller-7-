#Doc en google :D = https://docs.google.com/document/d/16Sni_DZvTVB_P6c-g6_EhHKQ1Gbw0bKjIhiwE0yVVdE/edit?usp=sharing

#Programa pa calcularas los valores propios y vecotres propios

import numpy as np #Importar la biblioteca numpy con un alias np
from numpy import linalg as LA #Importar el modulo de numpy que trabaja con funciones lineales y se le denomina el alias LA

a= np.array([[3,4],[5,6]]) #Crear arreglo de dos dimensiones por medio de una lista de listas (matriz cuadrada)
print(a) #Imprimir el arreglo

vrp,vp= LA.eig(a) #Se hace una asignacion multiple, en la cual vrp es valores propios y vp vectores propios
                  #Luego se llama la funcion de linial.eig el cual computa y realiza el calculo de valores y vectores propios de una matriz

print(vrp) #se imprime el resulatdo de el valor propio
print(vp) #Se imprime el resultado del vector propio