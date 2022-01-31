"""
Crear una clase Calificaciones.
Tendra un metodo init que admitira como entrada una lista de forma ['Raul', 9.2, 5, 4.5, 7, 9.1]
Tendra un metodo calificar que nos devolvera ['Raul', 'Notable']
"""

class Calificaciones():

    def __init__(self, alumno_notas=[]) -> None:

        if len(alumno_notas) >0:
            self.__nombre = alumno_notas[0]
            self.__notas = alumno_notas[1:]
            self.__calificacion = self.calcula_calificacion()
        else:
            self.__nombre = ''
            self.__notas = []
            self.__calificacion = ''

    def __str__(self) -> str:
        return f'Alumno: {self.__nombre} tiene la calificacion {self.__calificacion}'
        

    def calcula_calificacion(self):

        calificacion = ''
        if self.notas:            
            media_nota = sum(self.notas)/len(self.notas)
            if media_nota < 5:
                calificacion = 'SUSPENSO'
            elif 5<= media_nota <=5.4 :
                calificacion = 'SUFICIENTE'
            elif 5.5<= media_nota <=6.4:
                calificacion = 'BIEN'
            elif 6.5<= media_nota <=8.4 : 
                calificacion = 'NOTABLE'
            elif 8.5<= media_nota :
                calificacion = 'SOBRESALIENTE'
        else:
            calificacion = None

        return calificacion

    # def set_alumno(self,alum):
    #     self.nombre = alum[0]
    #     for elem in alum[1]:
    #         self.notas.append(elem)
    #         self.calificacion = self.calcula_calificacion()

    @property
    def alumno(self):
        return self.__nombre

    @alumno.setter
    def alumno(self, nuevo_alumno):
        self.__nombre = nuevo_alumno


    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self,nuevas_notas):
        self.__notas = nuevas_notas 
        self.__calificacion = self.calcula_calificacion()

    


