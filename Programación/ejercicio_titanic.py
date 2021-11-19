import os
import csv
import pprint   

os.system('clear')


ruta = '/home/raulsg/codigo/CursoDAM/Programación/csv/'

# 1- leer el archivo (como diccionario)
def leer_archivo():
    csv_in = open(ruta + 'titanic.csv') 
    lector_dic = csv.DictReader(csv_in)

    lista_dict = list(lector_dic)

    csv_in.close()
    return lista_dict


# 2- leer valores de campos survived
def leer_valores(persona):
    survivors = []
    titanic_list = leer_archivo()
    for persona in titanic_list:
        survivors.append(persona['Survived'])  
    return survivors 


# 3- contar (0=muerto, 1=vivo)
def contar_vivos_muertos():
    vivo = 0
    muerto = 0
    for number in leer_valores():
        if number == '1':
            vivo += 1
        else:
            muerto += 1
    return vivo, muerto

def clasifica_genero(persona):
    hombres = []
    mujeres = []
    for genero in persona:
        if persona['Sex'] == 'male':
            hombres.append(persona['Sex']) 
        elif persona['Sex'] == 'female':
            mujeres.append(persona['Sex'])   

# devolver resultado

v,m = contar_vivos_muertos()
print('vivo = {}'.format(v))
print('muertos = {}'.format(m))
print(clasifica_genero())

 



