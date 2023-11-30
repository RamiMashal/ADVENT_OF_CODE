import os
import pandas as pd

directorio_raiz = r'D:\RAMI\PROGRAMACION\USEFUL\useful_python\ADVENT_OF_CODE_2022\day7'
os.chdir(directorio_raiz)
# Por seguridad, aunque en el if tenemos que si el comando tiene 'cd' and '/' debemos volver a la carpeta day7, obligamos a iniciar el script en la ruta day7.
# Es código totalmente redundante.
print(f'Empezamos en la ruta: {os.getcwd()}')

with open(r'D:\RAMI\PROGRAMACION\USEFUL\useful_python\ADVENT_OF_CODE_2022\day7.txt', 'r') as day7:

    listas = [line.split(" ") for line in day7.read().strip().split('\n')]
    print(f'listas: {listas}')

for index, lista in enumerate(listas):
        
    if 'cd' and '/' in lista:
        os.chdir(directorio_raiz)
        # Este if solo sirve para la primera línea, aunque por seguridad lo dejo. No vaya a ser que haya más en el input y no me diera cuenta.
        print(f'Directorio actual: {os.getcwd()}')
    elif '$' and 'ls' in lista:
        if 'cd' and '/' in listas[index - 1]:
            os.chdir(directorio_raiz)
            # Este if solo sirve para la primera línea, porque si no hago el control, al ir a buscar listas[index - 1][2] ('/') cuando el comando es 'ls', nos devuelve al D:\ en el primer ls del input.
            print(f'Directorio actual: {os.getcwd()}')
        else:
            os.chdir(os.path.join(os.getcwd(), listas[index - 1][2]))
            print(f'Directorio actual: {os.getcwd()}')
            # Si es 'ls' significa que las siguientes líneas forman parte del directorio que se encuentra en la línea anterior al comando ls, por lo que, debemos entrar en ese directorio para crear las carpetas o ficheros.

    elif 'dir' in lista:

        if not os.path.exists(os.path.join(os.getcwd(), lista[1])):
            os.mkdir(os.path.join(os.getcwd(), lista[1]))
            # Quizá necesite hacer un chdir en la ruta una vez creada. Revisar la implicación de esto, porque creo que no llega a ser la solución.

    elif lista[0].isdigit():
        # Si el primer elemento es numérico, sabemos que hay que crear un fichero.
        open(os.path.join(os.getcwd(), f'{lista[0]}_{lista[1].replace(".", "")}.txt'), 'w').close()
    
    elif 'cd' and '..' in lista:
        os.chdir('..')

# Sacamos una lista con todos los paths del directorio_raiz.
# Además, la suma de los ficheros por directorio, sin importar si unos son subdirectorios de otros.

lista_paths = []
dict_dirs_sum_files = {}
sum_files = 0

for paths, dirs, files in os.walk(directorio_raiz):

    lista_paths.append(paths)

    # Por cada fichero del directorio, sumamos su tamaño
    if files:
        for file in files:
            sum_files += int(file.split('_')[0])

    # Creamos diccionario con el subdirectorio y la suma de los tamaños de sus ficheros. Este dict lo usaremos solo como mapeo.
    dict_dirs_sum_files[paths] = sum_files

    sum_files = 0 # Reseteamos la suma para no incluir el tamaño a otro directorio.

print(f'dict_dirs_sum_files: {dict_dirs_sum_files}')
print(len(dict_dirs_sum_files))

dict_dirs_total_sum = {} # Este diccionario suma los tamaños de los subdirectorios que contenga un directorio.
suma_total = 0

for path in lista_paths:
    for dir in dict_dirs_sum_files:
        if dir.startswith(path):
            suma_total = suma_total+dict_dirs_sum_files[dir]

    dict_dirs_total_sum[path] = suma_total
    suma_total = 0 # Reseteamos la suma para no incluir el tamaño a otro directorio.

print(f'dict_dirs_total_sum: {dict_dirs_total_sum}')
print(len(dict_dirs_total_sum))

dict_sum_100k = 0 # Variable para sumar el tamaño de los directorios con un tamaño <= 100.000

dirs_100k = []
for key in dict_dirs_total_sum:
    if dict_dirs_total_sum[key] <= 100000:
        dirs_100k.append([key, dict_dirs_total_sum[key]])
        dict_sum_100k += dict_dirs_total_sum[key]

print(f'La respuesta a la 1º parte es: {dict_sum_100k}')

# Para la segunda parte necesito el dict_dirs_total_sum para :
# variable que contenga la resta de 30.000.000 - (70.000.000 - directorio_raiz), para saber cómo de lejos estoy de 30.000.000
# luego tengo que encontrar el directorio con el tamaño más pequeño suficiente para liberar lo que falte para esos 30M.

size_para_liberar = 30000000 - (70000000 - dict_dirs_total_sum[directorio_raiz])
print(f'Necesito liberar: {size_para_liberar}')

# Saco los directorios con un tamaño >= a size_para_liberar
lista_sizes = [dict_dirs_total_sum[dir] for dir in dict_dirs_total_sum if dict_dirs_total_sum[dir] >= size_para_liberar]

print(f'La respuesta a la 2º parte es: {sorted(lista_sizes)[0]}') # En lugar de sorted() tienes el método min()