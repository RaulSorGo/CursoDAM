import pprint
import os

def clear():
    os .system('clear')


def datos_usuario():

    for i in range(100000000000):
        
        Nombre = input('Nombre: ')
        Apellido1 = input('Primer apellido: ')
        Apellido2 = input('Segundo apellido: ')
        Teléfono = input('Teléfono de contacto: ')
        Fecha_de_nacimiento = input('Fecha de nacimiento (dd/mm/aa): ')
        Pregun = input('¿Desea cambiar sus respuestas?, si o no. Introduzca su respuesta :  ')

        resultado = {'Nombre':Nombre,
         'Primer apellido':Apellido1,
         'Segundo apellido':Apellido2,
         'Teléfono':Teléfono,
         'Fecha de nacimiento':Fecha_de_nacimiento}

        if Pregun == str('no'):
            pprint.pprint(resultado)
            print('Que tenga un buen día :D')
            break
        else: 
            pass
    return resultado   

clear()
print(datos_usuario())