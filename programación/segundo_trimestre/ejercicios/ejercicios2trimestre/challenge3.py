statuses = {
    "Alice": "offline",
    "Bob": "online",
    "Eve": "online",
}
def online_count(statuses):
    contador = 0
    for estado in statuses:
        if estado[statuses] == 'online':
            contador+=1
    return(contador)
online_count(statuses)