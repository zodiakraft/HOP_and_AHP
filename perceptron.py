import random as rd
from prettytable import PrettyTable

col_map = 10
row_map = 10
map = [[0] * col_map] * row_map

headers = ['№']

# for i in map:
# 	print(i)
	
people = []

for i in range(rd.randint(0, 100)):
	people.append({
	'sex': 'male' if rd.randint(0, 1) == 0 else 'female',
	'age': rd.randint(0,100)})

for i in people[0]:
    headers.append(i)
    
table = PrettyTable(headers)

for i in range(len(people)):
	table.add_row([i + 1, people[i]['sex'], people[i]['age']])
print(table)