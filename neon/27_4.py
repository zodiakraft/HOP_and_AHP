f = open('274.txt')
x = f.readlines()
k58 = 0
k2 = 0
k29 = 0
for i in range(1, len(x)):
    if int(x[i])%58==0:
        k58 += 1
    if int(x[i])%2==0 and int(x[i])%58!=0:
        k2 += 1
    if int(x[i])%29==0 and int(x[i])%58!=0:
        k29 += 1
print(k58 * (k58 - 1) / 2 + k58 * (int(x[0]) - k58) + k2 * k29)
