"""
Hacer un programa que pida caracteres al usuario y los vaya guardando,
de forma que al finalizar muestre una lista con todas las vocales y otra 
con todas las consonantes. 
También debe contar cuantas hay en cada una de ellas
"""

def introduce_letra():
    vocales = []
    consonantes = []
    papelera = []
    cad = input('Introduzca todos los caracteres que desee: ')

    for letra in cad:
        if letra in 'aeiouAEIUO':
            vocales.append(letra)

        elif letra in 'qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM':
            consonantes.append(letra)
        else:
            papelera.append(letra)
    print(consonantes)
    print(len(consonantes))
    print(vocales)
    print(len(vocales))

introduce_letra()
