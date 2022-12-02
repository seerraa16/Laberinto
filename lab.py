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
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 


