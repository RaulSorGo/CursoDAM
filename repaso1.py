def pide_caracter():
    seguir = True
    vocales = ['a','e','i','o','u']

    while seguir:
        if input('Introduzca un caracter: ') == ' ':
            break
        elif input('Introduzca un caracter: ') in vocales:
            return f'VOCAL'
        else:
             return f'NO VOCAL'
        
pide_caracter()
