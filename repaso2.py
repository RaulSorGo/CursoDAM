"""
Hacer un programa que pida caracteres al usuario y los vaya guardando,
de forma que al finalizar muestre una lista con todas las vocales y otra 
con todas las consonantes. 
También debe contar cuantas hay en cada una de ellas
"""

def introduce_letra():
    vocales = []
    consonantes = []
    cad = input('Intrduzca todos los caracteres que desee: ')

    for letra in cad:
        if letra in 'aeiou':
            vocales.append(letra)
            print(vocales)
            print(len(vocales))
        else:
            consonantes.append(letra)
            print(consonantes)
            print(len(consonantes))

introduce_letra()
