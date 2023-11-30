# En cuántos pares de asignaciones un rango contiene totalmente al otro?

suma_parejas_solapadas = 0

with open('day4.txt', 'r') as day4:
    lista_parejas = [line.strip().split(',') for line in day4]

lista_numeros_separados = []
for pareja in lista_parejas:
    primera_pareja_numeros = pareja[0].split("-")
    segunda_pareja_numeros = pareja[1].split("-")
    lista_numeros_separados.append(primera_pareja_numeros + segunda_pareja_numeros)

for pareja in lista_numeros_separados:
    if int(pareja[0]) <= int(pareja[2]) and int(pareja[1]) >= int(pareja[3]) or \
        int(pareja[2]) <= int(pareja[0]) and int(pareja[3]) >= int(pareja[1]):

        suma_parejas_solapadas += 1

print(f'La respuesta a la 1º parte es: {suma_parejas_solapadas}')

############ SEGUNDA PARTE ############

# Ahora queremos saber el número, no solo aquellas parejas que se solapan por completo, sino de cualquiera que tenga un valor o rango solapado. Por tanto, con que uno de los números de una pareja se encuentre dentro del rango de la otra, ya sabemos que se solapa.
suma_parejas_solapadas2 = 0

for pareja in lista_numeros_separados:
    if  int(pareja[2]) <= int(pareja[0]) <= int(pareja[3]) or \
        int(pareja[2]) <= int(pareja[1]) <= int(pareja[3]) or \
        int(pareja[0]) <= int(pareja[2]) <= int(pareja[1]) or \
        int(pareja[0]) <= int(pareja[3]) <= int(pareja[1]):

        # Muy interesante, para esta comparación, podría usar la función range():
        # if pareja[0] is\in range(int(pareja[2]), int(pareja[3]))...(creo que funciona tanto con 'is' como con 'in'?)

        suma_parejas_solapadas2 += 1

print(f'La respuesta a la 2º parte es: {suma_parejas_solapadas2}')