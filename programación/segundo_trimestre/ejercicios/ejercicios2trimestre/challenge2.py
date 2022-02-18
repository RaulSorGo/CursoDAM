def mid(cadena):
    resto = len(cadena) % 2
    if resto == 0:
        return ""
    elif resto != 0:
        centro = len(cadena) // 2
        return cadena[centro]
print(mid("carsqaw5ehj"))