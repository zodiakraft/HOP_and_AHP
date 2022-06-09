b = []
print(1)


for i in range(100000):
    b.append('0'*100000)
print(1)

f = open("261.txt", 'r').readlines()
f = [i.split() for i in f]

    

for i in f:
    b[int(i[0])-1] = b[int(i[0])-1][:int(i[1])-1] + '1' + b[int(i[0])-1][int(i[1]):]

for i in range(len(b)):
    if '100000000000001' in b[i]:
        print(i+1, b[i].index('100000000000001') + 2)
