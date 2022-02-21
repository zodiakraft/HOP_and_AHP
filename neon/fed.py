a = int(input())
b = int(input())

c = ''

for i in range (a, b):
    c = c + str(i) + ' '

c += str(b)

print(c)