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
    

#Paso 5

nuevo = open(ruta_salida + '/lista_py.txt','w')
nuevo.write(fila)
nuevo.close()