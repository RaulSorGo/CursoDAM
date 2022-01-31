import os
import csv

os.system('clear')

ruta = '/home/raulsg/codigo/CursoDAM/Programación/csv/'

def csv_write():
    matriz = [
        [1,2,3,4,5,6],
        [3,4,5,6,7,7],
        [32,23,43,54,65,65],
        [44,55,6,6,7,8]
    ]

    with open(ruta + 'nuevo1.csv','a') as csv_writer:
        escritor = csv.writer(csv_writer) 
        escritor.writerow(['jueves']*10 + ['viernes'])
        escritor.writerow(['nada']*10 + ['fin'])

csv_write()