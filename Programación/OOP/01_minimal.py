import os
from pprint import pprint


def clear ():
    os.system('clear')
clear()

class Coche():
    matricula = None
    num_puertas = None
    color = None
    precio = None
    motor_en_marcha = False

    def __init__(self, matr, puertas, col, ):
        self.matricula = matr
        self.num_puertas = puertas
        self.color = col
        
    
    def __str__(self):
        return f'Matricula: {self.matricula}\nNúmero de puertas: {self.num_puertas}'

    def arrancar(self):
        self.motor_en_marcha = True
    
    def apagar(self):
        self.motor_en_marcha = False

bmw = Coche()
bmw.arrancar()
print('Motor: ', bmw.motor_en_marcha)

bmw.color = 'Verde'
bmw.matricula = '1234-QWE'  
bmw.num_puertas = '5'
bmw.precio = '200000'
bmw.marca = 'BMW'
bmw.modelo = 'Panda'
bmw.apagar()


print(bmw.color)
print(bmw.matricula)
print(bmw.num_puertas)
print(bmw.precio)
#pprint(dir(bmw))
# pprint(bmw.__class__)
# pprint(bmw.__dict__)
print(bmw)
bmw.apagar()
print('Motor: ', bmw.motor_en_marcha)
