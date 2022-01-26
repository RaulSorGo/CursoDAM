from random import randrange

def juego():
    winner = False
    jugador1 = jugador2 = 0
    tirada = 0
    while not winner       :
        tirada += 1
        jugador1 += randrange(1,6)
        jugador2 += randrange(1,6)
        print(f'Ronda: {tirada}\n    Jugador1: {jugador1} puntos\n    Jugador2: {jugador2} puntos')

        if jugador1 >= 100:
            mensaje_final = 'Jugador 1 '
            winner = True
        elif jugador2 >= 100:
            mensaje_final = 'Jugador 2'
            winner = True
        

    return f'Ganador: {mensaje_final} \n '


print(juego())
