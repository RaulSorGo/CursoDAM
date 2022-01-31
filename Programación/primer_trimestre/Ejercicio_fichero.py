# import os

# os.system('clear')

# RUTA = '/home/raulsg/codigo/CursoDAM/'
# DESTINO = '/Programación'
# carpeta = os.getcwd()

# nombres = os.scandir(carpeta)
# print(DESTINO)
# if a


# def rutas():
#     archivos = os.scandir()
# (-------------------------------------------------------------------------------------------------------------)

# Pasos para resolver el problema :

# 1. Buscar los archivos 
# 2. Seleccionar los archivos (Criba)
# 3. Procesar nombres de archivos (Quitar el .py)
# 4. Agruparlos de 5 en 5 
# 5. Guardar archivos en el fichero

import os 
import settings 

os.system('clear')

lista_archivo = []
archivo_salida = "salida.txt"
ruta_salida = settings.RUTA_BASE + settings.CODIGO + settings.MI_CARPETA
miembros = 5
fila = ''

#Pasos 1, 2 y 3

archivo = os.scandir(settings.RUTA_BASE + settings.CODIGO)
for a in archivo:
    if a.name.endswith('.py'):
        lista_archivo.append(a.name[:-3:])

#Paso 4

for i in range(0,len(lista_archivo),miembros):
    temp = lista_archivo[i: i+miembros]
    fila += ','.join(temp) + '\n'

#Paso 5

nuevo = open(ruta_salida + '/lista_py.txt','w')
nuevo.write(fila)
nuevo.close()
