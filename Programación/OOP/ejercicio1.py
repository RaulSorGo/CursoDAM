# Problema:
"""
Dada una cadena de texto, convertir cada carcater a su codigo ASCII.
Con eso creamos un numero formado por todos los codigos unidos, que llamaremos total_1.
Cambiar todos los numeros '7' por el numero '1', al que llamaremos total_2
Devolver la resta de total_1 - total_2
"""


def convertir(argu):
    total_1 = ''

    for i in argu:
        total_1 += str(ord(i))

    print(total_1)

    total_2 = total_1.replace('7','1')
    
    print(total_2)

convertir('CCC')