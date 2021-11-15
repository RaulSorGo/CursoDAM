def sumar(cadena):
    lista = cadena.split(',')
    for elem in lista:
        if not elem.isdigit():
            return "Error: No es un número"
    if len(lista)>2:
        return "Error: Demasiados números"
    elif len(lista) == 2:
        return True



def mas_de_dos_numeros_da_error():
    return sumar('1,2,3')

def dos_numeros_devuelve_true():
    return sumar('1,2') 

def valor_no_numericos_da_error():
    return sumar('1,r')

#--------------------------------------
print(mas_de_dos_numeros_da_error())
print(dos_numeros_devuelve_true())
print(valor_no_numericos_da_error())