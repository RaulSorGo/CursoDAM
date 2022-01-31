import os 
import pprint

os.system('clear')

ruta = '/home/raulsg/codigo/CursoDAM/Programación/viernes/programacion/python/lista_py.txt'
dic_salida = {}

def modo1 ():
#Leer archivo
    clave = 0
    with open(ruta) as archivo:
        for l in archivo:
    #Procesar fila a fila
            fila = l[:-1:].split(',')
    #Recorrer lista y llenar diccionario
            for nombre in fila:
                dic_salida[clave] = nombre
                clave += 1

def modo2():
    clave = 0
    texto = open(ruta,'r').readlines()
    pprint.pprint(texto)
    for archivo in texto:
        dic_salida[clave] = archivo
        clave += 1

        return dic_salida

pprint.pprint(modo2())