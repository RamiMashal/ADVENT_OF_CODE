import os
import pandas as pd

directorio_raiz = r'D:\RAMI\PROGRAMACION\USEFUL\useful_python\ADVENT_OF_CODE_2022\day7'
os.chdir(directorio_raiz)
# Por seguridad, aunque en el if tenemos que si el comando tiene 'cd' and '/' debemos volver a la carpeta day7, obligamos a iniciar el script en la ruta day7.
# Es código totalmente redundante.
print(f'Empezamos en la ruta: {os.getcwd()}')

with open(r'D:\RAMI\PROGRAMACION\USEFUL\useful_python\ADVENT_OF_CODE_2022\day7_prueba.txt', 'r') as day7:

    listas = [line.split(" ") for line in day7.read().strip().split('\n')]
    #listas.pop(0)
    print(listas)

for index, lista in enumerate(listas):

    if os.getcwd().startswith(directorio_raiz):
        # Este if es solo por seguridad, para que salga del bucle si me salgo del directorio haciendo pruebas y evitar crear cosas por ahí.
        # Utilizo startswith() porque si utilizo chdir() no podría moverme por los subdirectorios de day7, ya que saldría del bucle.
        # Con startswith() consigo hacer operaciones mientras la ruta se mantenga dentro del directorio_raiz.
        # Es código totalmente redundante.
        
        if 'cd' and '/' in lista:
            os.chdir(r'D:\RAMI\PROGRAMACION\USEFUL\useful_python\ADVENT_OF_CODE_2022\day7')
            # Este if solo sirve para la primera línea, aunque por seguridad lo dejo. No vaya a ser que haya más en el input y no me diera cuenta.
            print(os.getcwd())
        elif '$' and 'ls' in lista:
            if 'cd' and '/' in listas[index - 1]:
                os.chdir(r'D:\RAMI\PROGRAMACION\USEFUL\useful_python\ADVENT_OF_CODE_2022\day7')
                # Este if solo sirve para la primera línea, porque si no hago el control, al ir a buscar listas[index - 1][2] ('/') cuando el comando es 'ls', nos devuelve al D:\ en el primer ls del input.
                print(os.getcwd())
            else:
                os.chdir(os.path.join(os.getcwd(), listas[index - 1][2]))
                print(os.getcwd())
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

# Sacar la suma de los directorios cuyo tamaño es <= 100.000

dict_dirs_subdirs = {}
dict_dirs_sum_files = {}
lista_paths = []
sum_files = 0

for paths, dirs, files in os.walk(directorio_raiz):
    # Saco el directorio y los subdirectorios que contienen
    dict_dirs_subdirs[os.path.basename(paths)] = dirs

    # Por cada fichero del directorio, sumamos su tamaño
    if files:
        for file in files:
            sum_files += int(file.split('_')[0])

    # Creamos diccionario con el subdirectorio y la suma de los tamaños de sus ficheros
    dict_dirs_sum_files[os.path.basename(paths)] = sum_files
    lista_paths.append(paths)

    sum_files = 0

print(dict_dirs_subdirs)
print(dict_dirs_sum_files)

list_dirs_100k = [] # Creo lista para los directorios cuyo tamaño es <= 100.000
dict_sum_100k = 0 # Variable para sumar el tamaño de los directorios

for key in dict_dirs_sum_files:
    if dict_dirs_sum_files[key] <= 100000:
        dict_sum_100k += dict_dirs_sum_files[key]
        list_dirs_100k.append(key)


print(dict_sum_100k)
print(list_dirs_100k)

# Quiero los subdirectorios de los directorios cuyo tamaño es <= 100.000.

lista_subdirs_dirs100k = []
for paths, dirs, files in os.walk(directorio_raiz):
    if os.path.basename(paths) in list_dirs_100k:
        lista_subdirs_dirs100k += dirs

print(lista_subdirs_dirs100k)
print(len(lista_subdirs_dirs100k))

# Si los subdirectorios de los directorios cuyo tamaño es <= 100.000 aparecen en dict_dirs_sum_files significa que debo sumar su tamaño otra vez, puesto dicho tamaño también debería sumarse al directorio que lo contiene.
"""for key in dict_dirs_sum_files:
    if key in lista_subdirs_dirs100k:
        dict_sum_100k += dict_dirs_sum_files[key]"""

"""for key in lista_subdirs_dirs100k:
    if key in dict_dirs_sum_files:
        dict_sum_100k += dict_dirs_sum_files[key]


print(f'La respuesta a la 1º parte es: {dict_sum_100k}')"""

# Prueba esta parte en el script de pruebas a ver si es que el segundo código interfiere con lo de arriba y me está sumando de mas. Comprueba las 2 cifras las que saca

# Pensé que el problema es que estaba sumando duplicados, por lo que si usaba SET(lista_subdirs_dirs100k) quitaría duplicados y solo me sumaría una vez. Pero no es así, porque tanto si quito duplicados como si no, me da la misma cifra. Y aque lo que estoy comparando es si key in dict_dirs_sum_files: in lista_subdirs_dirs100k. Como evidentemente si está me suma solo el key de dict_dirs_sum_files.

# En relación con lo anterior, el problema no es que me sume duplicados, sino que no los sume. Ya que hay subdirectorios que aparecen en varios directorios, estos deberían sumarse el nº de veces que aparezcan en dichos directorios.

df_count_subdirs_dirs100k = pd.DataFrame({'SUBDIRS': lista_subdirs_dirs100k})
df_count_subdirs_dirs100k['COUNT'] = 1

df_count_subdirs_dirs100k = df_count_subdirs_dirs100k.groupby('SUBDIRS', as_index=False).agg('sum')

df_count_subdirs_dirs100k['SIZE'] = df_count_subdirs_dirs100k['SUBDIRS'].map(dict_dirs_sum_files)

# Los que no tienen fichero (no tienen tamaño) no nos interesan.
df_count_subdirs_dirs100k = df_count_subdirs_dirs100k.loc[df_count_subdirs_dirs100k['SIZE'] != 0]

df_count_subdirs_dirs100k['TOTAL_SIZE'] = df_count_subdirs_dirs100k['SIZE'] * df_count_subdirs_dirs100k['COUNT']

suma_total_dict_sum_100k = dict_sum_100k + df_count_subdirs_dirs100k['TOTAL_SIZE'].sum()

print(df_count_subdirs_dirs100k)
print(f'La respuesta a la 1º parte es: {suma_total_dict_sum_100k}')

# CREO QUE HE ENTENDIDO MAL EL EJERCICIO. SE TRATA DE BUSCAR LOS DIRECTORIOS CUYA SUMA TOTAL SEA COMO MÁXIMO 100.000, ENTRE TODOS!