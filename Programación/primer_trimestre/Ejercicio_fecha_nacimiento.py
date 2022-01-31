#pedir fecha de nacimiento 

def nacimiento():
    meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio',
     7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
    fecha = input('Introduzca fecha de nacimiento (dd/mm/aaaa):')
    partes = fecha.split('/')
    mensaje = 'Naciste el día ' + partes[0] + ' de ' + meses[int(partes[1])] + ' del año ' + partes[2]
    return mensaje

print(nacimiento())
