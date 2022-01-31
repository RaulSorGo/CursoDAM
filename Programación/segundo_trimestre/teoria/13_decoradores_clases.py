from datetime import date

class Persona():
    def __init__(self, nombre, apellido1, fecha_nacimiento) -> None:
        self.nombre = nombre
        self.apellido1 =apellido1
        self.fecha_nacimiento = fecha_nacimiento

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_fecha_nac(self):
        return self.__fecha_nacimiento

    def set_fecha_nacimiento(self,fecha):
        hoy = date.today() 
        fecha = date(1990, 1, 1)
        diferencia = hoy - fecha
        self.__fecha_nacimiento = fecha

p = Persona('teo','sanchez','1/1/2022')
p.set_fecha_nacimiento('01/01/2000')
p.get_fecha_nac()
print(p)