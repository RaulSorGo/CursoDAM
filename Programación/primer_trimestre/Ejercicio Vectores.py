# total = 0
# v1 = [1,2,3,4]
# v2 = [7,8,9,23]

# for x in range(len(v1)):
#     total += v1[x] * v2[x]
# print(total)

origen = [1,2,3,4,5,'Jose','Alan','Fernando']
numeros = []
alumnos = []
for x in origen:
    if type(x)==str:
        alumnos.append(x)
    else:
        numeros.append(x)
        
print(origen)
print(alumnos)
print(numeros)