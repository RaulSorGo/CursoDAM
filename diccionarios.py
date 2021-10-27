#repaso funciones

#funcio(a,b,c,d=1, *args, **kywargs)

diccionario = {
    'nombre': 'fernando',
    'apellido1':'lopez',
    'notas': [1,2,3,4,5]

}
diccionario['apellido2']= 'garcia'
diccionario['apellido1']= 'lópez'
print(type(diccionario))
print(diccionario['nombre'])
print(diccionario['apellido1'])
print(diccionario['apellido2'])
print(f"Nombre completo: {diccionario['nombre']} {diccionario['apellido1']}")
