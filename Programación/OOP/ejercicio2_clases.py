"""
Crea una clase NIF que se usará para mantener DNIs con su correspondiente letra.

Los atributos serán el número de DNI (entero largo) y la letra que le corresponde.

La clase dispondrá de los siguientes métodos:
Constructor predeterminado que inicialice el nº de DNI a 0 y la letra a espacio en
blanco (será un NIF no válido).

Constructor que reciba el DNI y establezca la letra que le corresponde.

Getters y setters para el número de DNI (que ajuste automáticamente la letra).

leer(): que pida el número de DNI (ajustando automáticamente la letra)
Método que nos permita mostrar el NIF (ocho dígitos, un guión y la letra en
mayúscula; por ejemplo: 00395469-F)

La letra se calculará con un método auxiliar (privado) de la siguiente forma:
se obtiene el resto de la división entera del número de DNI entre 23 y se usa la
siguiente tabla para obtener la letra que corresponde:
0  - T
7  - F
1  - R
8  - P
2  - W
9  - D  
3  - A
10 - X
4  - G
11 - B
5  - M
12 - N
6  – Y
13 – J
14 - Z
21 - K
15 - S
22 – E
16 - Q
17 - V 
18 - H
19 - L
20 – C
"""




class Nif():

    def __init__(self, num, letra) -> None:
        self.__num = num
        self.__letra = letra 

    def get_num(self):
        return self.__num 

    def set_num(self, num):
        self.__num = 
