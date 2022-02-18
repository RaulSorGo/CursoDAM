def double_letters(cadena):
    for i in range(len(cadena) - 1):
        letra1 = cadena[i]
        letra2 = cadena[i+1]
        if letra1 == letra2:
            return True
    return False

print(double_letters('anttonio'))