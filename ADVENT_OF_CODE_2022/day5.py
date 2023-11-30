# Para este ejercicio lo suyo sería controlar de numpy. En mi caso voy a intentar replicar la matriz input como una lista de listas. De esta forma evito lidiar con los nulos que tendrían las columnas de una matriz real.

# Utilizar el número negativo del primer número (el que indica la cantidad de cajas que tienes que coger), para que coja siempre las del final.
# Hacer un reverso de la lista para que la primera de la torre sea la primera que se coloca y, por tanto, las otras van encima.

""" La matriz real sería esta:
                    [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9 
"""

matriz = [
    ['B', 'Q', 'C'],
    ['R', 'Q', 'W', 'Z'],
    ['B', 'M', 'R', 'L', 'V'],
    ['C', 'Z', 'H', 'V', 'T', 'W'],
    ['D', 'Z', 'H', 'B', 'N', 'V', 'G'],
    ['H', 'N', 'P', 'C', 'J', 'F', 'V', 'Q'],
    ['D', 'G', 'T', 'R', 'W', 'Z', 'S'],
    ['C', 'G', 'M', 'N', 'B', 'W', 'Z', 'P'],
    ['N', 'J', 'B', 'M', 'W', 'Q', 'F', 'P'],
] # Nos imaginamos que cada lista es una columna. Esto lo he hardcodeado, pero molaría sacarlo leyendo del txt.

# Por cada movimiento me quedo solo con los indicadores de nº de cajas a mover y las posiciones de las columnas para quitar o añadir cajas.

with open('day5.txt', 'r') as day5:

    # Esto me devuelve un alista de listas con todas las frases tipo string.
    movimientos = [movimiento.split(" ") for movimiento in day5.read().strip().split("\n")]

# Quitamos todos los elementos que no sean números.
for movimiento in movimientos:
    for element in movimiento:
        if not element.isdigit():
            movimiento.remove(element)

for indicadores in movimientos:
    # Tenemos que convertir los indicadores a int porque todos los números de la lista movimientos son formato str.

    numero_cajas = int(indicadores[0]) * -1 # Quitamos el rango a partir del numero_cajas, entendido como la posición a partir de la cual quitar cajas. Lo convertimos en negativo para empezar el rango por el final.
    
    # Para sacar la posición de las columnas restamos uno debido a que el index de la matriz del ejercicio empieza en 1, pero el index de nuestra matriz empieza por cero ya que es una lista de listas.
    posicion_columna_quitar = int(indicadores[1]) - 1
    posicion_columna_poner = int(indicadores[2]) - 1

    columna_quitar = matriz[posicion_columna_quitar] # Hacemos una "copia" de la columna para sacar de ella las cajas correspondientes.

    rango_quitar = columna_quitar[numero_cajas:] # Nos quedamos con las cajas correspondientes para añadirlas a la columna correspondiente.
    #rango_quitar.reverse() # Aplicamos reverse para que la primera caja de la torre sea la primera en colocarse y las otras van encima.

    # PARA LA RESPUESTA 2, SOLO TENEMOS QUE COMENTAR EL REVERSE(), YA QUE SE PIDE EL MOVIMIENTO DE CAJAS SIN QUE EN EL MISMO ORDEN EN QUE SON EXTRAIDAS.
    
    # Este rango hay que sumarlo, para que añada los elementos de la lista, no la lista como un elemento.
    matriz[posicion_columna_poner] = matriz[posicion_columna_poner] + rango_quitar

    matriz[posicion_columna_quitar] = columna_quitar[0: numero_cajas] # En este slicing no se incluye la posición numero_cajas, lo que nos viene bien ya que esa posición pertenece a una caja que tiene que salir.

print(matriz)

top_cajas_mensage = ''

for posicion_columna in range(0, len(matriz)):
    top_cajas_mensage += matriz[posicion_columna][-1] # Para cada columna me quedo con la última letra.

print(f'La respuesta a la 1º y 2º parte es: {top_cajas_mensage}')

"""
# En lugar de usar remove(), podemos usar pop() combinado con range(). La razón es que remove() elimina la primera ocurrencia que encuentra, pero esa no es la caja correcta, queremos eliminar por el final. Así que eliminamos por posición negativa (por el final) con la ayuda de range().

for posicion in range(numero_cajas, 0):
    matriz[posicion_columna_quitar].pop() # No incluimos parámetro para que siempre borre la última.

Sin embargo, en vez de hacer un for con pop(), creo que es más eficiente aprovechar la variable columna_quitar (una copia de la columna de la que tenemos que quitar el rango y añadir a la otra) quedarnos con la slice que nos interesa usando la posición numero_cajas. De esta forma, en un solo paso, resignamos la columna entera solo con los elementos que le quedan después de perder las cajas correspondientes.
"""