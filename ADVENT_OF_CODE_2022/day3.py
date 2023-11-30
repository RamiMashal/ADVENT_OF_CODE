"""
Un elfo tiene la importante tarea de cargar todas las mochilas con provisiones para el viaje a la jungla. Desgraciadamente, ese elfo no ha seguido bien las instrucciones de empaquetado, por lo que ahora hay que reorganizar algunos objetos.

Cada mochila tiene dos grandes compartimentos. Todos los objetos de un mismo tipo deben ir exactamente en uno de los dos compartimentos. El elfo que ha hecho el equipaje no ha respetado esta regla y ha colocado exactamente un tipo de objeto por mochila.

Los elfos han hecho una lista de todos los objetos que hay actualmente en cada mochila (tu puzzle de entrada), pero necesitan tu ayuda para encontrar los errores. Cada tipo de objeto se identifica con una sola letra minúscula o mayúscula (es decir, a y A se refieren a tipos de objetos diferentes).

La lista de artículos de cada mochila se presenta en forma de caracteres en una sola línea. Una mochila determinada siempre tiene el mismo número de artículos en cada uno de sus dos compartimentos, por lo que la primera mitad de los caracteres representa los artículos del primer compartimento, mientras que la segunda mitad de los caracteres representa los artículos del segundo compartimento.

Por ejemplo, suponga que tiene la siguiente lista de contenidos de seis mochilas:

Por ejemplo, supongamos que tenemos la siguiente lista de contenidos de seis mochilas:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPZsGzwwsLwLmpwMDw

    La primera mochila contiene los artículos vJrwpWtwJgWrhcsFMMfFFhFp, lo que significa que su primer compartimento contiene los artículos vJrwpWtwJgWr, mientras que el segundo compartimento contiene los artículos hcsFMMfFFhFp. El único tipo de artículo que aparece en ambos compartimentos es la p minúscula.
    Los compartimentos de la segunda mochila contienen jqHRNqRjqzjGDLGL y rsFMfFZSrLrFZsSL. El único tipo de artículo que aparece en ambos compartimentos es la L mayúscula.
    Los compartimentos de la tercera mochila contienen PmmdzqPrV y vPwwTWBwg; el único tipo de artículo común es la P mayúscula.
    Los compartimentos de la cuarta mochila sólo comparten el tipo v.
    Los compartimentos de la quinta mochila sólo comparten el tipo de objeto t.
    Los compartimentos de la sexta mochila sólo comparten artículos del tipo s.

Para ayudar a priorizar la reordenación de elementos, cada tipo de elemento se puede convertir en una prioridad:

    Los elementos en minúsculas de la a a la z tienen prioridad del 1 al 26.
    Los elementos de la A a la Z en mayúsculas tienen prioridad del 27 al 52.

En el ejemplo anterior, la prioridad del tipo de artículo que aparece en ambos compartimentos de cada mochila es 16 (p), 38 (L), 42 (P), 22 (v), 20 (t) y 19 (s); la suma de estos es 157.

Encuentra el tipo de objeto que aparece en ambos compartimentos de cada mochila. ¿Cuál es la suma de las prioridades de esos tipos de objetos?
"""

# Separar las strings por la mitad.
# Creamos una lista de listas en la que guardamos cada línea dividida por la mitad en una lista. Luego comparamos la primera mitad con la segunda para sacar la letra común.

mochilas = []

with open('day3.txt', 'r') as day3:
    for mochila in day3:
        mitad = len(mochila)/2 # Debería haber usado // para que salga un int
        mochilas.append([mochila[0:int(mitad)], mochila[int(mitad):].replace('\n', "")])

# Sacamos la letra común entre las dos mitades de cada mochila, y las guardamos todas en una nueva lista.
# Las cadenas de textos tienen letras duplicadas, por lo que creamos una función para eliminarlas.

# ERES UN GRAN PARDILLO: SIMPLEMENTE GUARDANDO set(mochila[0:int(mitad)]) COMO UN SET(), AUTOMÁTICAMENTE BORRA LAS LETRAS DUPLICADAS
# SET ES UNA ESTRUCTURA DE DATOS QUE NO PERMITE DUPLICADOS.
def eliminar_letras_duplicadas(texto: str):
    for letra in texto:
        if texto.count(letra) > 1:
            texto = texto.replace(letra, "", texto.count(letra) - (texto.count(letra) - 1))
    return texto

letras_comunes = []

for mochila in mochilas:
    for letra in eliminar_letras_duplicadas(mochila[0]):
        # Solo necesitamos eliminar los duplicados de la primera mitad.
        if letra in mochila[1]:
            letras_comunes.append(letra) # En lugar de crear una lista con las letras y otra con las prioridades, podría sumar el index del diccionario de prioridades. Tanto el diccionario de prioridades como el for que lo asigna y la lista que crea son pasos de más.

# Usar enumerate para obtener la prioridad de las letras desde a-z hasta A-Z? (Contar como si fuera el alfabeto inglés 26 letras)

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Este alfabeto también lo podría haber hecho con la librería from string import ascii_letters

# Creamos un diccionario en el que cada letra tiene asociado el número de prioridad.

prioridades = {}

for index, letra in enumerate(alfabeto, start=1):
    # start = 1 para que no empiece a contar desde el cero.
    prioridades[letra] = index

# Creamos otra lista con las prioridades de las letras y la sumamos

prioridades_para_sumar = [prioridades[letra] for letra in letras_comunes]

print(len(alfabeto))
print(len(prioridades))
print(len(mochilas))
print(letras_comunes)
print(len(letras_comunes))

print(f'El resultado de la 1º parte es: {sum(prioridades_para_sumar)}')

##################### PARTE 2 #####################

"""
En lugar de una mochila dividida en 2, ahora hay que comparar las tres primeras líneas (mochilas), es decir, en grupos de 3 por mochila y sacar la letra común entre ellas.
"""
mochilas2 = []

with open('day3.txt', 'r') as day3:
    for mochila2 in day3:
        mochilas2.append(mochila2.replace('\n', ""))
print(len(mochilas2))
mochilas_grupos = []
counter = 0
for mochila2 in mochilas2:
    # En lugar de crear un counter y usarlo a mi manera, podría usar for i in range(0, len(data), 3): # En pasos de 3. rucksacks = data[i:counter] Pero counter empezaría en 3.
    mochilas_grupos.append([mochilas2[counter], mochilas2[counter + 1], mochilas2[counter + 2]])
    if counter == 297:
        break
    counter += 3

print(len(mochilas_grupos))

letras_comunes2 = []

for mochila2 in mochilas_grupos:
    for letra in eliminar_letras_duplicadas(mochila2[0]):
        # Solo necesitamos eliminar los duplicados de la primera mitad.
        if letra in mochila2[1] and letra in mochila2[2]:
            letras_comunes2.append(letra)

# Creamos otra lista con las prioridades de las letras y la sumamos

prioridades_para_sumar_grupos = [prioridades[letra] for letra in letras_comunes2]
print(len(prioridades_para_sumar_grupos))
print(letras_comunes2)
print(len(letras_comunes2))

print(f'El resultado de la 2º parte es: {sum(prioridades_para_sumar_grupos)}')
