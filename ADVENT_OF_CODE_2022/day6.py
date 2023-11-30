# Necesitamos encontrar el primer grupo de 4 letras que sean diferentes entre ellas, y proporcionar el marcador: la posición de la última letra de dicho grupo.

# Deberíamos descartar las primeras 4 letras por separado?, ya que si miramos 4 posiciones hacia atrás a partir de las 3 primeras posiciones nos salta el error out of index.

with open('day6.txt', 'r') as day6:
    texto_completo = day6.read()

texto_completo = [letra for letra in texto_completo]

posiciones_marcadores = []
for index, letra in enumerate(texto_completo):
    array_4_ultimas_letras = texto_completo[index - 14: index] # LA RESPUESTA 2 SOLO NECESITA CAMBIAR ESE NÚMERO DE 4 A 14.
    # Por cada letra, me quedo con las 4 últimas letras excepto dicha letra, que es la siguiente a la última letra que cierra el grupo de 4. Si el grupo de 4 contiene letras diferentes, el índice de esa letra es el marcador.
    # Parece que no da error out of index cuando resto 4 posiciones a las 3 primeras letras. Devuelve 4 listas vacías.

    if len(set(array_4_ultimas_letras)) == 14:
        # Dado que set es una estructura de datos que elimina los duplicados, si len() es menor que 4 significa que había duplicados y ese grupo no sirve como marcador.
        # LA RESPUESTA 2 SOLO NECESITA CAMBIAR ESE NÚMERO DE 4 A 14.

        posiciones_marcadores.append([index, letra]) # Aunque solo queremos el index, entendido además como nº de caracteres a recorrer para encontrar el marcador, guardamos también la letra, que debe ser la siguiente a la última letra que cierra el grupo de 4.

print(f'La respuesta a la 1º y 2º parte es: {posiciones_marcadores[0][0]}')




