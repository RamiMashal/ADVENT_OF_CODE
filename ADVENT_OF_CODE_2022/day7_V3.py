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

"""
Este código es redundante con el elif '$' and 'ls' in lista:. La razón es que, mientras estén los 2 códigos, le estamos pidiendo a python que entre 2 veces en el mismo sitio y devuelve algo como esto 'D:\\RAMI\\PROGRAMACION\\USEFUL\\useful_python\\ADVENT_OF_CODE_2022\\day7\\a\\a'. Para evitarlo, dejemos el control de 'ls', porque siempre que aparece un 'ls', la línea anterior es un $ cd letra.

elif len(lista) == 3 and lista[0] == '$' and lista[2].isalpha():
    # Si la lista contiene 3 elementos, el primero es $ y el tercero es una letra, sabemos que debemos ejecutar chdir al directorio que marque la letra.
    print(lista)
    os.chdir(os.path.join(os.getcwd(), lista[2]))
    print(os.path.join(os.getcwd(), lista[2]))
"""

# Sacamos los directorios con los subdirs que contienen.

lista_paths = []

for paths, dirs, files in os.walk(directorio_raiz):
    lista_paths.append(paths)
print(lista_paths)
print(len(lista_paths))

lista_dirs_subdirs = [] # Esta lista almacenará todos los subdirectorios de cada path
global_dict_dirs_subdirs = {} # Este diccionario almacenará el path con todos los subdirectorios de lista_dirs_subdirs

for path in lista_paths:
    for paths, dirs, files in os.walk(path):
        lista_dirs_subdirs = lista_dirs_subdirs + dirs

    global_dict_dirs_subdirs[os.path.basename(path)] = lista_dirs_subdirs

    lista_dirs_subdirs = [] # Reseteamos esta lista para no repetir los subdirectorios en el siguiente path.

# Damos una segunda vuelta para sacar todos los directorios, sin importar si unos son subdirectorios de otros, y la suma de los tamaños de los ficheros que contienen. Para esto basta con iterar únicamente el directorio_raiz.

dict_dirs_sum_files = {}
sum_files = 0

for paths, dirs, files in os.walk(directorio_raiz):

    # Por cada fichero del directorio, sumamos su tamaño
    if files:
        for file in files:
            sum_files += int(file.split('_')[0])

    # Creamos diccionario con el subdirectorio y la suma de los tamaños de sus ficheros. Este dict lo usaremos solo como mapeo.
    dict_dirs_sum_files[os.path.basename(paths)] = sum_files

    sum_files = 0

print(f'global_dict: {global_dict_dirs_subdirs}')
print(len(global_dict_dirs_subdirs))
print(f'dict_dirs_sum_files: {dict_dirs_sum_files}')
print(len(dict_dirs_sum_files))

# A cada directorio de dict_dirs_sum_files le tenemos que sumar el tamaño de los ficheros de los subdirectorios que contenga.
for dir in dict_dirs_sum_files:
    for subdir in global_dict_dirs_subdirs[dir]:
        dict_dirs_sum_files[dir] = dict_dirs_sum_files[dir] + dict_dirs_sum_files[subdir]

print(f'dict_dirs_sum_files: {dict_dirs_sum_files}')
print(len(dict_dirs_sum_files))

dict_sum_100k = 0 # Variable para sumar el tamaño de los directorios

dirs_100k = []
for key in dict_dirs_sum_files:
    if dict_dirs_sum_files[key] <= 100000:
        dirs_100k.append([key, dict_dirs_sum_files[key]])
        dict_sum_100k += dict_dirs_sum_files[key]

print(f'dict_sum_100k: {dict_sum_100k}')
print(f'dirs_100k: {dirs_100k}')
print(f'dirs_100k len: {len(dirs_100k)}')



