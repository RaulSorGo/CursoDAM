#Raul Soriano Gomez


class Persona():
    nombre = None
    apellidos = None
    edad = None
    dni = None

    def __init__(self, nombre, apellidos, edad, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.dni = dni 

    def __str__(self):
        return f'Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad}\nDNI: {self.dni}'

pers = Persona(nombre= input('Introduzca Nombre: '), apellidos= input('Introduzca apellidos: '), edad=input('Introduzca su edad: '), dni=input('Introduzca DNI: '))

def solicita_personas(pers):
    lista_personas = []
    for continuar in pers:
        while input('¿Desea continuar?: ') != 'No' or 'no':
            lista_personas.append(pers)

        if input('¿Desea continuar?: ') == 'Si' or 'si' :
            
            break

    return lista_personas

solicita_personas(Persona)

