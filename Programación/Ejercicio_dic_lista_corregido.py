import os 
import pprint

os.system('clear')

ruta = '/home/raulsg/codigo/CursoDAM/Programación/viernes/programacion/python/lista_py.txt'
dic_salida = {}
clave = 0

#Leer archivo
with open(ruta) as archivo:
    for l in archivo:
#Procesar fila a fila
        fila = l[:-1:].split(',')
#Recorrer lista y llenar diccionario
        for nombre in fila:
            dic_salida[clave] = nombre
            clave += 1

pprint.pprint(dic_salida)