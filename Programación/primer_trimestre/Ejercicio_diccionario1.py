AFORO_MAXIMO = 3

def introduce():
    personas = {}

    for i in range (1200):
        if i == AFORO_MAXIMO:
            break
        nombre = input('Introduzca nombre:')
        apellidos = input('Introduzca apellido:')
        dni = input('Introduzca DNI:')
        personas[dni] = {"nombre":nombre , "apellidos":apellidos}

    return personas

print(introduce())
