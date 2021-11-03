def introduce():
    personas = {}

    for i in range (5):
        nombre = input('Introduzca nombre:')
        apellidos = input('Introduzca apellido:')
        dni = input('Introduzca DNI:')
        personas[dni] = {"nombre":nombre , "apellidos":apellidos}

    return personas

print(introduce())
