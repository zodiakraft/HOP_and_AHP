file = open('26.txt', 'r')
lines = (file.readline()).split()
first = int(lines[0])
second = int(lines[1])
third = int(lines[2])
l1st = [0] * first

for i in range(first):
    lines = file.readline()
    l1st[i] = int(lines)

for i in range(len(l1st)):
    for j in range(len(l1st) - 1):
        if l1st[j] < l1st[j + 1]:
            index = l1st[j]
            l1st[j] = l1st[j + 1]
            l1st[j + 1] = index

for i in range(second):
    l1st_2 = l1st[i]
    l1st[i] = -1

for i in range(len(l1st)):
    for j in range(len(l1st) - 1):
        if l1st[j] < l1st[j + 1]:
            index = l1st[j]
            l1st[j] = l1st[j + 1]
            l1st[j + 1] = index

for i in range(third):
    l1st_1 = l1st[i]

print(l1st_1, l1st_2)

# 520 910