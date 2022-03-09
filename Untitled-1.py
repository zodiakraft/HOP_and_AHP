from sympy import symbols, solve

formules_symbols = ['c', 'A', 'B', 'N', 'v', 'S', 't', 'p', 'm', 'V', 'pr', 'F', 'S', 'g', 'h']

for i in formules_symbols:
	globals()[i] = symbols(i)

#print(globals())

h = 2.4
p = 710
g = 10
formules = [(A-B)/N-c, S/t-v, S/t-v, v+v-v, p/V-m, F/S-pr, p*g*h-pr, h/h-p/p, F/F-S/S, p*g*V-F]

output = round(solve(formules[6], pr)[0], 2)

if '.00' in str(output):
	print(int(output))
elif str(output)[-1] == '0':
	print(round(output, 1))
else:
	print(output)