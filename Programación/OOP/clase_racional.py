def enuncioado():

    #Constructor que admita numerador y denominador
    #Constructor sin parametros
    #Metodos getters y setters
    #suma, resta, multiplicacion y division
    pass

import os

def clear():
    os.system('clear')
clear()

class Fraccion():
#Definimos el init y pasamos los valores de numerador y denominador como type = int

    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        if denominador == 0:
            raise Exception("El denominador no puede ser 0")
        self.denominador = int(denominador)

#Convertimos el type = int de los valores anteriores a type = str para poder representar visualmente la fraccion

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

#Averiguamos el MCD para poder sumar y restar fracciones que no tengan el mismo denominador 

    # def maximo_comun_divisor(self, a, b):
    #     temporal = 0
    #     while b != 0:
    #         temporal = b
    #         b = a % b
    #         a = temporal
    #     return a

def getnumerador(self):
        return self.numerador

def getdenominador(self):
        return self.denominador




    

