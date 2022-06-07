f = open('27-B.txt', 'r').readlines()
f = [int(i) for i in f]
del f[0]

n = 1000000
s = 0

b = []
g = []
d = 0

otvet = 0

for i in range(n):
    s += min([i, n-i])*f[i]
    if i < n//2:
        b.append(f[i])
    else: g.append(f[i])
    
b = sum(b)
g = sum(g)
d = s
l = d
s = 0

for i in range(1, n):
    b = b - f[i-1] + f[(i + n//2 - 1)%n]
    g = g - f[(i + n//2 - 1)%n] + f[i-1]
    d = d - b + g
    if d < l:
        l = d
        otvet = i+1

print(l)
print(otvet)
# for j in range(1, n): #Мусорный завод
#     s += min([abs(k-j), n-abs(k-j)]) * f[k] #Мусорные баки
#     b.append(s)

    # b = b - f[i] + f[((i+n-1)//2)%n]
    # g = g - f[(((i - 1 +n)//2) + 1)%n] + f[i]