import numpy as np

matrix = np.array([[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], dtype='int16')
print(matrix)

row, col = np.indices((5, 5)) #, sparse=True
print()
print(row)

lista_indices_filas = []

for fila in row:
    for indice in fila:
        lista_indices_filas.append(indice)

print(lista_indices_filas)
print(col)

lista_indices_columnas = []
for fila in col:
    for indice in fila:
        lista_indices_columnas.append(indice)

print(lista_indices_columnas)

lista_posiciones = list(zip(lista_indices_filas, lista_indices_columnas))
print(lista_posiciones)

print(matrix[row, col])

lista_arboles_visibles = []

for posicion in lista_posiciones:
    #  Si el size de algún array es 0 el árbol sería visible porque es un borde, y ya no haría falta seguir con com la comparación de <>
    print(f'Arbol a comprobar: {matrix[posicion[0], posicion[1]]}') # Unbound me devuelve siempre 0, usa el debug a ver si rascas algo.
    #print(matrix[posicion[0], posicion[1]+1:]) # Derecha
    #print(matrix[posicion[0], :posicion[1]]) # Izquierda
    #print(matrix[:posicion[0], posicion[1]]) # Arriba
    #print(matrix[posicion[0]+1:, posicion[1]]) # Abajo

    if matrix[posicion[0], :posicion[1]].size == 0 \
        or matrix[posicion[0], posicion[1]+1:].size == 0 \
        or matrix[:posicion[0], posicion[1]].size == 0 \
        or matrix[posicion[0]+1:, posicion[1]].size == 0 \
        or matrix[posicion[0], posicion[1]] > max(matrix[posicion[0], :posicion[1]]) \
        or matrix[posicion[0], posicion[1]] > max(matrix[posicion[0], posicion[1]+1:]) \
        or matrix[posicion[0], posicion[1]] > max(matrix[:posicion[0], posicion[1]]) \
        or matrix[posicion[0], posicion[1]] > max(matrix[posicion[0]+1:, posicion[1]]):
        lista_arboles_visibles.append(matrix[posicion[0], posicion[1]])

print(lista_arboles_visibles)
print(f'La respuesta a la 1º parte es: {len(lista_arboles_visibles)}')

scenic_score = []

for posicion in lista_posiciones:
    print(f'Arbol a comprobar: {matrix[posicion[0], posicion[1]]}')

    if matrix[posicion[0], :posicion[1]].size == 0 \
        or matrix[posicion[0], posicion[1]+1:].size == 0 \
        or matrix[:posicion[0], posicion[1]].size == 0 \
        or matrix[posicion[0]+1:, posicion[1]].size == 0:
        scenic_score.append(0)
        print(f'scenic_score: {scenic_score}')
    else:
        # arboles_izquierda
        counter = 0
        for tree in list(reversed(matrix[posicion[0], :posicion[1]])):
            counter += 1
            if tree >= matrix[posicion[0], posicion[1]]:
                arboles_izquierda = counter
                print(f'arboles_izquierda: {arboles_izquierda} es mayor')
                break
            arboles_izquierda = counter

            print(f'arboles_izquierda: {arboles_izquierda} no es mayor')
        # arboles_derecha
        counter = 0
        for tree in matrix[posicion[0], posicion[1]+1:]:
            counter += 1
            if tree >= matrix[posicion[0], posicion[1]]:
                arboles_derecha = counter
                print(f'arboles_derecha: {arboles_derecha} es mayor')
                break
            arboles_derecha = counter

            print(f'arboles_derecha: {arboles_derecha} no es mayor')
        # arboles_arriba
        counter = 0
        for tree in list(reversed(matrix[:posicion[0], posicion[1]])):
            counter += 1
            if tree >= matrix[posicion[0], posicion[1]]:
                arboles_arriba = counter
                print(f'arboles_arriba: {arboles_arriba} es mayor')
                break
            arboles_arriba = counter

            print(f'arboles_arriba: {arboles_arriba} no es mayor')

        # arboles_abajo
        counter = 0
        for tree in list(matrix[posicion[0]+1:, posicion[1]]):
            counter += 1
            if tree >= matrix[posicion[0], posicion[1]]:
                arboles_abajo = counter
                print(f'arboles_abajo: {arboles_abajo} es mayor')
                break
            arboles_abajo = counter

            print(f'arboles_abajo: {arboles_abajo} no es mayor')
        
        scenic_score.append(arboles_izquierda*arboles_derecha*arboles_arriba*arboles_abajo)

print(f'scenic_score: {scenic_score}')
print(f'La respuesta a la 2º parte es:: {max(scenic_score)}')
"""
Quizá no haya que rallarse tanto. No queremos contar los arboles solo cuando se encuentre uno igual o mayor, sino que queremos saber cuantos arboles puede ver hasta encontrarse con uno igual o mayor que el.
Así que no necesitamos saber la posición de dichos arboles, sino aumentar un contador hasta encontrarse con uno. Así para las 4 direcciones, y multiplicar estos números.



Dale una vuelta aunque creo que también se complica eso de contar.
Si el arbol es un borde, le asignamos 0, porque su multiplicación daría 0.
# TEN EN CUENTA ESTO: Para la IZQUIERDA Y ARRIBA tienes que hacer reverse() de las listas, ya que numpy crealos elementos en el orden de aparición, y nosotros queremos empezar a contar desde el más cercano al árbol a comprobar.
"""



