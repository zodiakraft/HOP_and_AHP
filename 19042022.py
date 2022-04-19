file = open('26_22.txt', 'r').readlines()
max = file[0].split()[0]
del file[0]

k = 0
n = 0
file = sorted(file)
max = int(max) - int(file[-1])

for i in range(len(file)):
    if k+int(file[i]) <= int(max):
        k += int(file[i])
        n += 1
    else:
        if str(max-k) <= file[i]:
            n += 1
        print(n)
        print(file[-1])
        break
