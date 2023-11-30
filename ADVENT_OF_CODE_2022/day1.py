

"""
Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

Ejemplo:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000


The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

import pandas as pd

# Pasamos toda la lista a un txt y creamos una copia en csv. Por cada línea del txt asignamos un elfo cuyo nombre cambiará (usamos un counter para elfo1, elfo2, etc) cada vez que una línea sea un salto de línea \n. De esta forma, sabemos que número pertenece a cada elfo (Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.).

counter = 1

with open('day1.txt', 'r') as puzzle_1:
    with open('day1_copy.csv', 'w') as puzzle_copy: 
        for line in puzzle_1:
            if line == '\n':
                counter += 1
            puzzle_copy.write(f'elf{counter};{line}')

calories_by_elf = pd.read_csv('day1_copy.csv', sep=';', names=['elfs', 'calories'])

print(calories_by_elf.dtypes)
# No nos importan los elfos que no tienen número, ya que rellenamos los na con 0 para hacer la suma total por cada elfo.
calories_by_elf.fillna(0.0, inplace=True)

print(calories_by_elf)

calories_by_elf_sum = calories_by_elf.groupby('elfs').agg('sum').sort_values(by='calories', ascending=False)

print('La respuesta a la 1º parte es:')
print(calories_by_elf_sum.head(1))
# La segunda parte de la prueba es calcular la suma del top 3 de calorías recogidas por elfos.
sum_top_three = calories_by_elf_sum['calories'][0] + calories_by_elf_sum['calories'][1] + calories_by_elf_sum['calories'][2] 
print(f'La respuesta a la 2º parte es: {sum_top_three}')