from operator import itemgetter

f = open("272.txt")
n = int(f.readline())
data = f.readlines()
del data[0]

index = 0

c = []
d = []

for i in range(0, n - 1):
    for j in range(0, n - 1):
        if i != j:
            if abs(int(data[i]) - int(data[j])) %2 == 0:
                if int(data[i]) % 17 == 0 or int(data[j]) % 17 == 0:
                    c.append([index, int(data[i]) + int(data[j])])
                    d.append([index, int(data[i]), int(data[j])])
                    index += 1

c = sorted(c, key=itemgetter(1))
print(c[-1])
for i in d:
    if i[0] == c[-1][0]:
        print(i)
