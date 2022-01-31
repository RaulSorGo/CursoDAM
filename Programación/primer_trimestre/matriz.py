# lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in range(20):
#     x = lista
#     print(x)

import pprint

cols=10
filas=10
matriz=[]

for i in range(filas):
    fila=[]
    for j in range(cols):
        fila.append(f"{i}-{j}")
    matriz.append(fila)
pprint.pprint(matriz)