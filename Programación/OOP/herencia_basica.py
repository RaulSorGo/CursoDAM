class Base():
    datos = []


class Hijo1(Base):
    def __init__(self, elemento): 
        self.datos.append(elemento)


class Hijo2(Base):
    def __init__(self, elemento):    
        self.datos.append(elemento)

h1 = Hijo1('Hijo1')
h2 = Hijo2('Hijo2')

print(h1)
print(h2)

print(h1.datos)
print(h2.datos)