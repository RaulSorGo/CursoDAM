cadena=('uno, dos, tres, cuatro, cinco')
inicio= 0
trozo=''
resultado=[]
num_comas=cadena.count(',')+1

for i in range(num_comas):
    final=cadena.find(',',inicio)
    if final== -1:
        trozo=cadena[inicio:]
    else:
        trozo=cadena[inicio:final]
        resultado.append(trozo.strip())
        inicio=final+1

print(resultado)