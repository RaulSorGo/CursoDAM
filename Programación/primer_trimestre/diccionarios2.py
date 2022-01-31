from pprint import pprint

d = {}
d1 = dict([
    ('clave1', 1),
    ('clave2', 2),
    ('clave3', 3),
    ('clave4', 4)
    ])


d1['fruta'] = ['manzana','pera','uva']

#añadir elementos

v1 = d1['fruta']
v1.append('platano')
v1.append('sandia')
d1['fruta'] = v1

print(d1['clave1'])
pprint(d1)

#borrar elementos

del(d1['clave1'])
pprint(d1)

#obtener todas las claves

claves = d1.keys()
pprint(claves)

#obtener todos los valores

valores = d1.values()
pprint(valores)

#iterar sobre un diccionario

for k in  d1:
    print(k,d1[k])

for k,v in d1.items():
    print(f'clave:{k} valor: {v}')

#limpiar en un diccionario

#d1.clear()
#print(d1)

#elementos de un diccionario
print(d1.items())

#extraer elementos de un diccionario

#elem = d1.pop('fruta')

d1['ultimo'] = 'FIN'
elem = d1.popitem()
print(elem)
print(d1)