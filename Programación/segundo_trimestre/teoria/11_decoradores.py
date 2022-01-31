"""
Son funciones que admiten funciones como parámetro y devuelven funciones
"""



def mi_decorador(funcion):
    def deco1(*args, **kwargs):
        print('-----------Empiezo a decorar')
        c = funcion(*args, **kwargs)
        print(c)
        print('----------.Fin de la decoracion')
        
    return deco1

@mi_decorador
def saludar():
    print('HOLA MUNDO!!!')

#saludar()

# resp = mi_decorador(saludar)
# resp()

@mi_decorador
def sumar(a,b):
    return a + b

print(sumar(1,2))

# @mi_decorador
# def restar(a,b):
#     return a- b 