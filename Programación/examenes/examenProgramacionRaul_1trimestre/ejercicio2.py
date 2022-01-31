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


pers = Persona(nombre='Raúl', apellidos='Soriano Gómez', edad='19', dni='123456789A')



print(pers)              