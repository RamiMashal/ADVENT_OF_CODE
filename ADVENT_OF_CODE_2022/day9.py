"""
Documentación útil

* Eliminar duplicados de una lista de listas: https://stackoverflow.com/questions/2213923/removing-duplicates-from-a-list-of-lists
    * Al parecer no funciona convetir una lista de listas en set, me da TypeError: unhashable type: 'list', pero si funciona con tuplas.

"""

"""
REGLAS

* Cabeza y cola deben tocarse siempre, diagonalmente adyacentes e incluso superpuestas.
* Cuenta todas las posiciones que la cola visitó al menos una vez. Esto me sugiera que no hay que contar dos veces la misma posición.
* Importante esto: si la cabeza y la cola no se tocan, y no están en la misma fila, la cola siempre se mueve un paso en diagonal para seguir el ritmo. Es ddecir, que si están en distinta row no tienes que hacer dos pasos de 90 grados, si no que te colocas en la misma row con un solo paso diagonal. Esto es importante, porque debemos tener esto en cuenta para no sumar una podisción de más.

* Doy por sentado, ya que no se menciona nada al respecto, que los movimientos nunca se van a salir de la matriz, por lo que no me preocupo por los errores out of scope. ERROR, si que puedes salirte del scope, pero lo estoy solucionando haciendo una matriz grande por la ambigüedad del enunciado al respecto. No sirve con hacer una matrix de max_moves.

OBJETIVOS

* Calcular la posición de la cabeza.
* En función de dicha posición, cómo saber si la cola está tocando?
IDEAS

* Para saber el tamaño que debe tener la matriz habrá que hacer un max de los números (posiciones).

* Cómo saber si se están tocando.

* Parece obvio que debemos saber las coordenadas de la cabeza y la cola por toda la matriz. Ya que, además de saber si se están tocando, necesitamos almacenar el número de posiciones por las que ha pasado la cola.

* Función para calcular la suma o resta de las posiciones en ambos ejes? Tomaría como parámetros el movimiento (u,d,l,f) y la posición actual, para devolver la posición de la cabeza.

    * Crear cuatro funciones diferentes para cada movimiento, ya que cada movimiento_posición se hace de uno en uno, es decir, no nos movemos arriba y a la derecha a la vez, sino que se hace en dos tiempos.

    * Crear un diccionario de funciones para que se mapearlas en la función general que serán llamadas según el parámetro de movimiento.

* Crear una lista donde vamos almacenando las nuevas posiciones, convertirla en un set al final para que me quite duplicados directamente? Al parecer solo funciona con tuplas, porque con lista de listas me da TypeError: unhashable type: 'list'. 
    lista = {(1,1), (1,1), (1,2)}

    set = set(lista)

    print(set)

* para saber el nº de posiciones que ha visitado la cola, quizá ir recopilando en una lista las posiciones y hacer un simple count? En caso de que no haya que tener en cuenta las posiciones repetidas habrá que eliminar dichas posiciones de la lista.
"""

from typing import List, Tuple
import math
import numpy as np

################################# Procesando el fichero para obtener los movimientos y el número de posiciones.
# Así mismo, establecemos la posición inicial, en la que empiecan cabeza y cola.

with open("day9.txt", "r") as file:

    moves_positions_orders = [tuple(el.strip().split(" ")) for el in file.readlines()]

print(moves_positions_orders)

#max_moves = max([int(el[1]) for el in moves_positions_orders]) # Hago un max de los movimientos para saber el shape de la matriz (Ejemplo: 5).

max_moves = 1000

start_position = [round(max_moves / 2), round(max_moves / 2)] #start_position = [max_moves - 1, 0] # La cabeza y la cola empiezan superpuestas abajo a la izquierda. Restamos 1 al max_moves para que no se salga de rango, ya que, por ejemplo, en una matriz de (5,5) los índices van de 0 a 4.

# RECUERDA QUE SI HACES LA MATRIZ MÁS GRANDE TENDRAS QUE ADAPTAR LA STARTING POSITION DE CABEZA Y COLA, ESE DECIR, QUE NO DEPENDEN DEL MAX_MOVES.

print(f'start_position: {start_position}\n')

################################# Creamos una matriz de ceros y creamos una lista de índices de las posiciones de la misma
# La dimensión filas y columnas de la matriz será el máximo número del input.
# Reutilizo el código del ejercicio day8, sin crear la lista_posiciones, ya que no nos hace falta.

head_position = start_position

tail_position = start_position

matrix = np.zeros((max_moves + 1, max_moves + 1))#np.random.randint(10, size=(max_moves, max_moves)) #  Utilizo una matriz de random ints al principio para facilitar trackear las posiciones haciendo pruebas. Cuando funciones podría usar la matriz de ceros para convertir a 1 las posiciones por las que pasa la cola.

matrix[start_position[0], start_position[1]] = 1 # Dejamos marcada la posición de inicio porque también cuenta como casilla que visita la cola.

#print(matrix)
#print(start_position)
#print('start position')
#print(matrix[start_position])
#print(matrix[start_position[0], start_position[1]])
#print('end')

################################# Calculamos las posiciones en función de las órdenes

def check_is_touching(head_position:List[int], tail_position:List[int]) -> bool:
    # Recuerda que esta función solo la tienes que aplicar en la parte de la cola, si no la cabeza también se parará.

    if head_position == tail_position:
        print("Se tocan, por tanto, la cola no se mueve.")
        return True

    if head_position[0] == tail_position[0] and abs(head_position[1] - tail_position[1]) == 1:
        # Uso abs() para ahorrarme comprobar quién está a la derecha o izquierda, mientras que la distancia no sea mayor que 1 posición.
        print("Se tocan, por tanto, la cola no se mueve.")
        return True

    if abs(head_position[0] - tail_position[0]) == 1 and (abs(head_position[1] - tail_position[1]) == 1 or head_position[1] == tail_position[1]):
        # Aquí, además de comprobar que la distancia a izquierda o derecha sea igual a 1, también hay que comprobar si están en la misma columna.
        print("Se tocan, por tanto, la cola no se mueve.")
        return True

    return False

#print(check_is_touching([2, 2], [1, 2])) # Para pruebas

tail_positions = [tuple(start_position)] # Creamos una lista (más tarde lidiaremos con los duplicados) donde almacenamos las posiciones de la lista. Incluimos la posición inicial, ya que las 2 empiezan ahí solapadas y también se cuenta.
# Convertimos las posiciones en tuplas porque el set(), que usamos para quitar posiciones duplicadas al final, solo funciona con una lista de tuplas. Si intentamos hacer un set con una lista de listas nos da TypeError: unhashable type: 'list'.

for move_position in moves_positions_orders:
    if move_position[0] == "R":
        head_position = [head_position[0], head_position[1] + int(move_position[1])]
        matrix[head_position[0], head_position[1]] = 1 # Voy pintando las casillas de la cabeza (solo la posición final) como ayuda.

        if not check_is_touching(head_position, tail_position):
            # Ten en cuenta que en la R y D empezamos el for por la tail, ya que izquierda y abajo es sumar.
            for num in range(tail_position[1] + 1, head_position[1]):
                tail_position = [head_position[0], num]
                matrix[tail_position[0], tail_position[1]] = 2 # Voy pintando TODAS las posiciones de la cola. Solo como ayuda.

                tail_positions.append(tuple(tail_position)) # Añado cada posición por la que debe pasar la cola.
            
        print(f'HEAD: {head_position}, {move_position}')
        print(f'TAIL: {tail_position}, {move_position}')
        #print(tail_positions)
        #print(matrix)
    
    elif move_position[0] == "L":
        head_position = [head_position[0], head_position[1] - int(move_position[1])]
        matrix[head_position[0], head_position[1]] = 1

        if not check_is_touching(head_position, tail_position):
            # Hacemos reversed en todas menos en R, ya que si no el for nos da posiciones de 0 a n, pero necesitamos de n a 0, ya que en una matriz abajo es sumar, arriba es restar, etc. En la R  y D no hace falta porque la izquierda y abajo es sumar.
            # Volvemos a convertir en list() porque el reversed devuelve un objeto.
            for num in list(reversed(range(head_position[1] + 1, tail_position[1]))):
                tail_position = [head_position[0], num]
                matrix[tail_position[0], tail_position[1]] = 2

                tail_positions.append(tuple(tail_position))

        print(f'HEAD: {head_position}, {move_position}')
        print(f'TAIL: {tail_position}, {move_position}')
        #print(tail_positions)
        #print(matrix)
    
    elif move_position[0] == "U":
        head_position = [head_position[0] - int(move_position[1]), head_position[1]] # RECUERDA que subir es restar a las posiciones de las rows!
        matrix[head_position[0], head_position[1]] = 1
    
        if not check_is_touching(head_position, tail_position):
            for num in list(reversed(range(head_position[0] + 1, tail_position[0]))):
                # aHORA ENTIENDO QUE HAY QUE JUGAR CON LAS POSICIONES DE LA CABEZA Y COLA, ESTÁ MAL EL IF DE LA RIGHT, FUNCIONA PORQUE ES EL PRIMER MOVIMIENTO. ARREGLA ESO Y REPLICALO SEGÚN LAS CIRCUNSTANCIAS. COMO PUEDES VER, SI USAS LAS POSICIONES DE LA CABEZA O COLA, NO TENDRÁS EL PROBLEMA DEL MOVIMIENTO DIAGONAL. FIJATE QUE, EN EL UP, LA tail_position TOMA LAS POSICIONES DEL NUM Y LA CABEZA PARA LA COLUMNAS, POR LO QUE, INVOLUNTARIAMENTE, RESOLVEMOS LOS DIAGONALES.
                # aDEMAS, SUMANDO UNO (EN EL CASO DE UP) PARA LAS POSICIONES DE FILA DE LA CABEZA NOS POSICIONAMOS DETRÁS DE LA MISMA SIN SOLAPARLA, COMO DEBE SER PARA NO CONTAR TAMPOCO ESA POSICIÓN.
                tail_position = [num, head_position[1]]
                matrix[tail_position[0], tail_position[1]] = 2

                tail_positions.append(tuple(tail_position))

        print(f'HEAD: {head_position}, {move_position}')
        print(f'TAIL: {tail_position}, {move_position}')
        #print(tail_positions)
        #print(matrix)
    
    elif move_position[0] == "D":
        head_position = [head_position[0] + int(move_position[1]), head_position[1]] # RECUERDA que bajar es sumar a las posiciones de las rows!
        matrix[head_position[0], head_position[1]] = 1

        if not check_is_touching(head_position, tail_position):
            for num in range(tail_position[0] + 1, head_position[0]):
                tail_position = [num, head_position[1]]
                matrix[tail_position[0], tail_position[1]] = 2

                tail_positions.append(tuple(tail_position))

        print(f'HEAD: {head_position}, {move_position}')
        print(f'TAIL: {tail_position}, {move_position}')
        #print(tail_positions)
        #print(matrix)

print(f'La respuesta a la primera pregunta es: {len(set(tail_positions))}') # Los convertimos a set() para que nos quite posiciones duplicadas.

# CUIDADO PORQUE, AUNQUE LA L, R y U han funcionado:

# Tendrás que decidir si incluir por defecto la posición inicial en la lista y sumar o restar 1 en el for de la R, ya que al principio empiezan en 4, 0 y te viene bien para que cuente esta posición y no tener que meter la posición inicial de la lista. Pero esto hará que falle a lo largo del camino. Simplemente podría usar después un quitar duplicados, pero mejor hacer limpio sea de una forma o de otra.

# En el primer down no funciona la función check_is_touching. Estoy casi seguro de que es porque, aunque todo se pinte bien, las posisciones que va tomando la cola no son correctas, ya que hay que invertir los rangos en algunos casos. Busca la mejor forma de invertir los rangos para que la posición de la cola sea la correcta y calcule bien el siguiente movimiento.

def move_right(current_position:List[List[int]]) -> List[List[int]]:
    """
    Adds 1 position from column-axis

    Args:
        move_position (List): [row, column]

    Returns:
        List: new position = [row, column]
    """
    new_position = [current_position[0], current_position[1] + 1]

    return new_position

def move_left(current_position:List[List[int]]) -> List[List[int]]:
    """
    Subtracts 1 position from column-axis

    Args:
        current_position (List): [row, column]

    Returns:
        List: new position = [row, column]
    """
    
    new_position = [current_position[0], current_position[1] - 1]

    return new_position

def move_up(current_position:List[List[int]]) -> List[List[int]]:
    """
    Adds 1 position from row-axis

    Args:
        current_position (List): [row, column]

    Returns:
        List: new position = [row, column]
    """

    new_position = [current_position[0] + 1, current_position[1]]

    return new_position

def move_down(current_position:List[List[int]]) -> List[List[int]]:
    """
    Subtracts 1 position from row-axis

    Args:
        current_position (List): [row, column]

    Returns:
        List: new position = [row, column]
    """
    new_position = [current_position[0] - 1, current_position[1]]

    return new_position

def move_position_controller(move_position_order:Tuple[str, int], current_position:List[List[int]]) -> List[List[int]]:
    pass
"""
MOVES_FUNCTIONS = {
    "R": move_right(),
    "L": move_left(),
    "U": move_up(),
    "D": move_down()
}
"""
""" COMENTARIOS ANTIGUOS.

# LA CONCULSION POR LA QUE ME FALLA  (r, 4) desdpues del ('D', '1') es por que se me va de rango, porque yo entendí que hacer una matriz del max_moves era lo logico, lo di por sentado. El ejercicio menciona que hay que trazar en una matriz bidimensional, por lo que yo entendí que con un max_moves tengo el numero de col y rows. Pero, si no consigo entender el ejercicio, porque no especifica el rango de la matriz, hago una matriz lo enorme y hasta ta no me falle.

# Los movimientos los hace bien hasta que se va fuera de rango, por lo que tengo que entender bien si el enunciado especifica el bien el rango o no.
# ESTOY SEGURO QUE HAY UNA FORMA MATEMATICA DE SACAR EL TAMAÑO MINIMO DE UNA MATRIZ A PARTIR DE SUS POSICIONES RANDOM.
# Solucines a probar: 
    # crear una matriz grande y rezar porque funcione.
    # Intentar que la matriz solo crezca a medida que lo pidan las posiciones, como un juego en el que vas descubriendo nuevo terreno.
    # Averiguar si se puede calcular la dimensión necesaria a partir de las posiciones?
    # RECUERDA QUE SI HACES LA MATRIZ MÁS GRANDE TENDRAS QUE ADAPTAR LA STARTING POSITION DE CABEZA Y COLA, ESE DECIR, QUE NO DEPENDEN DEL MAX_MOVES.

# Sea como sea, tengo que sacar el movimiento diagonal, porque si no estaré contando más posiciones de las que se necesitan.
    # Creo que tendría que tendría que sacar movimientos diagolanes para arriba y abajo, e izquierda y derecha en ambos sentidos.

# Cómo detectar que la cabeza a cabiado de fila y me tengo que mover diagonalmente?
    # Y cómo saber que, en caso de estar la cabeza inmediatamente arriba o abajo, y si se mueve otra vez hacia arriba o abajo, no me tengo que mover diagonalmente?

    # IMPORTANTE ESTO: Esto es una rallada, dale una vuelta porque quizá sea más sencillo de lo que parece. 

# Cómo saber que, tras el movimiento de la cabeza, sigo tocando, por lo que no tengo que hacer nada?

# CREO QUE LA SOLUCIÓN SERÍA IR SUMANDO EL NÚMERO DE POSICIONES DE LAS ÓRDENES MENOS 1, ES DECIR, LOS PASOS QUE VA DANDO LA CABEZA MENOS 1, PORQUE LA COLA SIEMPRE VA POR DETRÁS, Y EL MOVIMIENTO DIAGONAL NOS EVITA CONTAR DOS PASOS. El problema es saber cuándo la cabeza se mueve y no tienes que moverte porque estás tocando.
    # Para, no solo contar las posiciones de la cola, sino también pintarlas en la matriz, ya que solo pintamos las posiciones finales, podríamos hacer un for con las posiciones de la cabeza menos 1 y pintar todas esas posiciones. Es decir, pintar todos los pasos de la cola.

# REPITE LA COMPROBACIÓN DE QUE ESTÁS HACIENDO EL CAMINO BIEN PARA LA CABEZA Y LA COLA, AHORA QUE HAS METIDO LA FUNCIÓN IS TOUCHING.
# SOLUCIONA EL PROBLEMA DE CÓMO CONTAR Y NO SUMAR MÁS POSICIONES CON LOS PASOS DIAGONALES. FÍJATE EN EL SEGUNDO PASO DE ('R', '4') PARA TENER EN CUENTA ESTA PROBLEMA.

# Quizá me equivoque pero se me ocurre que, una vez que tenemos la función is touching, lo que mantiene a la cola sin moverse, debería comparar la última posición de la cola con la nueva, así sabré cuántos pasos he dado. Creo que funcionaría sumando la resta con abs entre las columnas y lo mismo para las filas.
    # Aunque podríamos hacerlos así, creo que lo mejor es ir almacenando todas las posiciones de la cola, porque algunas se repiten y debemos quitar duplicados. Usa un set de tuplas, ya que las listas no funcionan con set.

# Has conseguido la primera parte para guardar las posiciones cde la cola en una lista. Para la izquierda será igual de fácil de la derecha, pero para el movimiento diagonal y arriba vas a necesitar tener en cuenta también las filas.
    # Como puedes ver, la diagonal va a ser más complicado, porque ahora te pinta más posiciones de las que son.
"""
