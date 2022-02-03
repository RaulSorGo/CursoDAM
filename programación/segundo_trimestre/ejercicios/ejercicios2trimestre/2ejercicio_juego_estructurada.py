from random import randrange

def juego():
    winner = False
    j1 = input('Introduzca nombre Jugador 1:')
    j2 = input('Introduzca nombre Jugador 2:')
    jugador1 = 0 
    jugador2 = 0
    tirada = 0
    while not winner:
        tirada += 1
        jugador1 += randrange(1,7)
        jugador2 += randrange(1,7)
        print(f'Ronda: {tirada}\n    Jugador1: {jugador1} puntos\n    Jugador2: {jugador2} puntos')

        if jugador1 >= 100:
            mensaje_final = j1
            winner = True
        elif jugador2 >= 100:
            mensaje_final = j2
            winner = True
        

    return f'Y el ganador es...:\n¡¡¡{mensaje_final}!!!'


print(juego())
