import numpy as np

lista_trees = []

with open('day8.txt', 'r') as day8:
    for trees in day8.readlines():

        row_trees = [int(tree) for tree in trees.strip()]
        lista_trees.append(row_trees)

matrix = np.array(lista_trees, dtype='int16')

print(matrix) # Esto no lo imprimo porque son muchos

print(f'Matrix shape: {matrix.shape}')
print(f'Matrix size: {matrix.size}')
print(f'Matrix ndim: {matrix.ndim}')
print(f'Matrix type: {type(matrix)}')

# Saco una matrix idéntica con las posiciones sustituyendo a los números reales (árboles)

row, col = np.indices((matrix.shape[0], matrix.shape[1])) # Utilizo el shape de la matrix en nº de filas y columnas.

#print(f'Matrix rows position:\n\n{row}') # Esto no lo imprimo porque son muchos
#print(f'Matrix col position:\n\n{col}')

lista_indices_filas = [] # Hago una lista para poder zipear con las posiciones de las columnas.

for fila in row:
    for indice in fila:
        lista_indices_filas.append(indice)

#print(f'lista_indices_filas: {lista_indices_filas}') # Esto no lo imprimo porque son muchos

# print(f'Matrix rows position:\n\n{col}') # Esto no lo imprimo porque son muchos

lista_indices_columnas = [] # Hago una lista para poder zipear con las posiciones de las filas.
for fila in col:
    for indice in fila:
        lista_indices_columnas.append(indice)

#print(f'lista_indices_columnas: {lista_indices_columnas}') # Esto no lo imprimo porque son muchos

lista_posiciones = list(zip(lista_indices_filas, lista_indices_columnas)) # Lp convierto en lista porque sino devuelve una memoria.
#print(f'lista_posiciones: {lista_posiciones}') # Esto no lo imprimo porque son muchos

#print(f'matrix[row, col]:\n\n{matrix[row, col]}') # Pasando la matrix de row y col a matrix, te devuelve los números reales. Esto no lo vamos a usar, es solo para que eniendas la utilidad de np.indices() # Esto no lo imprimo porque son muchos

"""
#print(matrix[posicion[0], posicion[1]+1:]) # Derecha
#print(matrix[posicion[0], :posicion[1]]) # Izquierda
#print(matrix[:posicion[0], posicion[1]]) # Arriba
#print(matrix[posicion[0]+1:, posicion[1]]) # Abajo
"""

lista_arboles_visibles = []

for posicion in lista_posiciones:
    #  Si el size de algún array es 0 el árbol sería visible porque es un borde, y ya no haría falta seguir con com la comparación de >
    # print(f'Arbol a comprobar: {matrix[posicion[0], posicion[1]]}') # Esto no lo imprimo porque son muchos

    if matrix[posicion[0], :posicion[1]].size == 0 \
        or matrix[posicion[0], posicion[1]+1:].size == 0 \
        or matrix[:posicion[0], posicion[1]].size == 0 \
        or matrix[posicion[0]+1:, posicion[1]].size == 0 \
        or matrix[posicion[0], posicion[1]] > max(matrix[posicion[0], :posicion[1]]) \
        or matrix[posicion[0], posicion[1]] > max(matrix[posicion[0], posicion[1]+1:]) \
        or matrix[posicion[0], posicion[1]] > max(matrix[:posicion[0], posicion[1]]) \
        or matrix[posicion[0], posicion[1]] > max(matrix[posicion[0]+1:, posicion[1]]):
        # Los max() me resultan muy útiles para sacar el número mayor de los arrays.
        lista_arboles_visibles.append(matrix[posicion[0], posicion[1]])

print(f'La respuesta a la 1º parte es: {len(lista_arboles_visibles)}')

"""
Para la 2º parte necesitamos saber cuántos árboles son visibles desde el punto de vista de cada árbol (de izquierda a derecha y de arriba abajo). El resultado es la multiplicación del nº de árboles visibles en los 4 sentidos. Si un árbol es mayor que el árbol a comprobar cortamos la cuenta de árboles, ya que no se puede ver más allá de un árbol igual o superior.

Mi solución con 4 for es bastante guarra pero no se me ocurrió otra forma de hacerlo.

Si el arbol es un borde, le asignamos 0, porque su multiplicación daría 0, obvio.

TEN EN CUENTA ESTO: Para la IZQUIERDA Y ARRIBA tienes que hacer reverse() de las listas, ya que numpy crea los elementos del array en el orden en el que están colocados en la matriz, y nosotros queremos empezar a contar desde el más cercano al árbol a comprobar.
"""
scenic_score = []

for posicion in lista_posiciones:

    if matrix[posicion[0], :posicion[1]].size == 0 \
        or matrix[posicion[0], posicion[1]+1:].size == 0 \
        or matrix[:posicion[0], posicion[1]].size == 0 \
        or matrix[posicion[0]+1:, posicion[1]].size == 0:
        scenic_score.append(0)

    else:
        # arboles_izquierda
        counter = 0
        for tree in list(reversed(matrix[posicion[0], :posicion[1]])):
            counter += 1 # Vamos contando árboles hasta que llegamos al final o nos encontremos un igual o superior al árbol a comprobar.
            if tree >= matrix[posicion[0], posicion[1]]:
                arboles_izquierda = counter
                break
            arboles_izquierda = counter

        # arboles_derecha
        counter = 0
        for tree in matrix[posicion[0], posicion[1]+1:]:
            counter += 1
            if tree >= matrix[posicion[0], posicion[1]]:
                arboles_derecha = counter
                break
            arboles_derecha = counter

        # arboles_arriba
        counter = 0
        for tree in list(reversed(matrix[:posicion[0], posicion[1]])):
            counter += 1
            if tree >= matrix[posicion[0], posicion[1]]:
                arboles_arriba = counter
                break
            arboles_arriba = counter

        # arboles_abajo
        counter = 0
        for tree in list(matrix[posicion[0]+1:, posicion[1]]):
            counter += 1
            if tree >= matrix[posicion[0], posicion[1]]:
                arboles_abajo = counter
                break
            arboles_abajo = counter
        
        scenic_score.append(arboles_izquierda*arboles_derecha*arboles_arriba*arboles_abajo)

print(f'La respuesta a la 2º parte es:: {max(scenic_score)}')
