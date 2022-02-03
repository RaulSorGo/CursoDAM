def sumar(arg):
    total = 0
    for val in arg:
        
        if type(val) is not int:
            return 0

    if type(arg) == tuple:
        return 0

     

    
    
    return total

def no_hay_argumentos_devuelve_cero():
    return sumar('')

def lista_enteros_floats_devuelve_suma():
    return sumar(['-5','8.6','-2'])

def cadena_de_texto_devuelve_cero():
    return sumar('holi')

def numeros_complejos_devuelve_cero():
    return sumar(4j)

def objetos_no_numericos_devuelve_cero():
    return sumar('a')


print(no_hay_argumentos_devuelve_cero())

print(lista_enteros_floats_devuelve_suma())

print(cadena_de_texto_devuelve_cero())

print(objetos_no_numericos_devuelve_cero())

print(numeros_complejos_devuelve_cero())
