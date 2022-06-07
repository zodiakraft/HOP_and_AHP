f = open('27-B.txt', 'r').readlines()
f = [int(i) for i in f]
del f[0]

n = 1000000
s = 0

b = []

for j in range(n): #Мусорный завод
    for k in range(n):
        s += min([abs(k-j), n-abs(k-j)]) * f[k] #Мусорные баки
    b.append(s)
    s = 0
print(b.index(min(b))+1)
print(min(b))