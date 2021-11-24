import csv
import os

archivo = '/home/raulsg/codigo/CursoDAM/Programación/csv/titanic.csv'

def leer_dict():
    csv_in = open(archivo)
    lector_dict = csv.DictReader(csv_in)

    lista_dict = list(lector_dict)

    csv_in.close()
    return lista_dict

def escribe_archivo():
    for p in persona:



