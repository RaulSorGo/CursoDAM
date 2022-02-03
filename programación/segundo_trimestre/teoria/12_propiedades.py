#Decorador para comprobar si los parametros son enteros

def son_enteros(funcion):
    def envoltura(*args):
        for i in args:
            if not type(i) is int:
                raise Exception('Parametros no enteros')
        return funcion(*args)
        #Hacer mas cosas 
    return envoltura    


#Multiplicacion de numeros enteros 
@son_enteros
def multiplicacion(a,b):
    return a*b

resp = multiplicacion(2,6)
print(resp)