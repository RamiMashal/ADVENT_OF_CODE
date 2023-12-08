# Matrix

* El uso de la matrix es trivial, solo lo hago para pintar las casillas y hacerlo más visual para ayudarme.

    * Más tarde lidiaremos con cómo saber el tamaño que debería tener una matriz para que no de fallo.
        * Se me ocurre que, una vez sabiendo el max_moves, y sabiendo el número de movimientos que vamos a tener que hacer, el tamño que debería tener una matriz serí multiplicar el max_moves por el número de movimientos. Porque, imagina que los 2000 movimientos fueran todos a la derecha moviendote cada vez el max_moves. Sería una posibilidad. Pero pintar esto sería una locura. Por eso, me parece bien la idea de abrir camino a medida que se va necesitando, como si fuera un video juego en el que descubres terreno.

* El core de la función son los if para mapear las direcciones y sumar o restar las posiciones indicadas, además de la función check_is_touching.

# Core: Direcciones y posiciones y check_is_touching

# check_is_touching

* Para pensar: check_is_touching es **realmente necesaria? Creo que si** porque, aunque en el for ya lidiamos con calcular las posiciones de la cola a partir de la cabeza, sumando 1 para que no nos cuente la posición actual (lo que nos quita duplicados, salvo el caso que pasemos varias veces por la misma casilla), tenemos el problema de que si la cabeza sube o baja aunque solo sea una casilla, la cola se pondrá detrás de ella.

# Direcciones y posiciones.

* Creo que debería diferenciar entre el cálculo de los movimientos de la cabeza y la cola. Tanto en la 1º como en la 2º parte la cabeza marca el camino, por tanto es independiente.

# Mapear posiciones y aplicar la función correspondiente.

* Quizá sea bueno rescatar la idea de un controler, con vistar a poder usar esa función recursivmente en la segunda parte?

# Pasos:

1. Funciones separadas para cabeza y cola con los parámetros que necesiten.

# 2º parte Ideas

# Recursividad

* Aplica en este ejercicio?

# Cabeza y colas

* Está claro que la función para calcular las posiciones de la cola la podemos reutilizar. Pero funcionará la función de la cola para las 9 posiciones de la serpiente?

* Para hacerlo pro, debemos pensar en crear una solución que funcione para 9 o las n casillas que pueda tener la serpiente.

* Quizá crear una variable (int) con el número de casillas que debe ocupar la serpiente y, en función de eso, combinar el for de moves_positions_orders con una función recursiva que se repita tantas veces como longitud debe tener la serpiente? Y quedarnos con el último resultado, es decir, la posición de la cola de la serpiente.

* Hay que tener en cuenta que, excepto para la cabeza y la cola reales, cada posición de la serpiente es una cabeza y una cola a la vez, que debe seguir el mismo patrón que la serpiente de 2 posiciones de longitud.



