import pprint

cols=10
filas=10
matriz=[]

for i in range(filas):
    fila=[]
    for j in range(cols):
        fila.append("x")
    matriz.append(fila)
# pprint.pprint(matriz)


#-----------------

for i in range(filas):
    linea=''
    for j in range(cols):
        linea+=matriz[i][j]
    print(linea)
#deberes para mañna, multiplicar matrices 3x3
# M=1,2,3
#   4,5,6
#   7,8,9

# H=9,8,7
#   6,5,4
#   3,2,1

