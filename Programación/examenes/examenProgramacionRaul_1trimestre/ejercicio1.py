#Raul Soriano Gomez

from pprint import pprint
import os

ruta= '/home/raulsg/Desktop/examenProgramacionRaul/'


# def leer_archivo():
#     cadena =()
#     resultado = []
#     with open(ruta + 'palabras.txt.TXT') as archivo:
#         palabras = archivo.readlines()
#         for palabra in archivo:
#             palabras.append(cadena)

#         for palabra in cadena:
#             if {'e'} not in palabra:
#                 resultado.append(palabra)
#     print(resultado) 
            

# leer_archivo()

def clear():
    os.system('clear')

archivo = open(ruta + 'palabras.txt.TXT')
palabras = archivo.read()
lista_palabras = palabras.split("\n")   


#Este bloque  abre, lee, extrae el contenido, elimina el signo de salto de linea y luego lo cierra.

def palabras_sin_e():
    lista_inicial = lista_palabras
    lista_final = []
    for palabra in lista_inicial:
        if 'e' not in palabra:
            lista_final.append(palabra)

#esta funcion se encarga de buscar la letra e en cada elemento de la lista que le hemos pasado y añadirlas a una lista nueva. 

    return lista_final

def cierra_archivo():
    archivo.close()

clear()
pprint(palabras_sin_e())   



