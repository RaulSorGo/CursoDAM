import os 
import settings 

os.system('clear')

lista_archivo = []
archivo_salida = "salida.txt"
ruta_salida = settings.RUTA_BASE + settings.CODIGO + settings.MI_CARPETA
miembros = 5



def busca_archivo():
    archivo = os.scandir(settings.RUTA_BASE + settings.CODIGO)
    for a in archivo:
        if a.name.endswith('.py'):
            lista_archivo.append(a.name[:-3:])
    return lista_archivo


def escribe_archivo(lista_archivo, miembros):
    fila = ''
    for i in range(0,len(lista_archivo),miembros):
        temp = lista_archivo[i: i+miembros]
        fila += ','.join(temp) + '\n'
    return fila[:-1:]

# def dic_lista(fila):
#lfila = len(escribe_archivo(any,5))
# diclist = []
# #for x in range(len(escribe_archivo(any,5))):
# diclist.append(len(escribe_archivo(lista_archivo,5)))
# print(diclist) 

#No funciona