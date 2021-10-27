#repaso funciones

#funcio(a,b,c,d=1, *args, **kywargs)

#diccionarios


# diccionario = {
#     'nombre': 'fernando',
#     'apellido1':'lopez',
#     'notas': [1,2,3,4,5]

# }
# diccionario['apellido2']= 'garcia'
# diccionario['apellido1']= 'lópez'
# print(type(diccionario))
# print(diccionario['nombre'])
# print(diccionario['apellido1'])
# print(diccionario['apellido2'])
# print(f"Nombre completo: {diccionario['nombre']} {diccionario['apellido1']}")

# import pprint

# vscode={
#       "version": "0.2.0",
#     "configurations": [
#         {
#             "name": "Python: Archivo actual",
#             "type": "python",
#             "request": "launch",
#             "program": "${file}",
#             "console": "integratedTerminal"
#         }
#     ]
# }
# vscode['configurations'][0]['type']= 'manolito'
# tmp = vscode
# pprint.pprint(tmp)

#Mi primer diccionario

from pprint import PrettyPrinter, pprint


variable = [('campo1','valor1'),
            ('campo2','valor2'),
            ('campo3','valor3'),
            ('campo4','valor4'),
            ('campo5','valor5'),
            ('campo6','valor6')]

dic=dict(variable)
pprint(dic.items())

#procesar diccionarios 

for k,v in dic.items() :
    print(k,v)

#-------------------------

claves = dic.keys()
valores = dic.values()
pprint(claves)
pprint(valores)

for c in list(claves):
    print(c)

