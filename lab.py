def laberinto(dimension, muros):
    laberinto = [
    ['E', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]
    for i in range(dimension):
        fila = []
        for j in range(dimension):
            if tuple([i, j]) in muro:
                fila.append('X')
            else:
                fila.append(' ')
        laberinto.append(fila)
    return laberinto


