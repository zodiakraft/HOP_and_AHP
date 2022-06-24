a = []
print(0)
for i in range(100000):
    a.append('0' * 100000)
print(1)
f = open('261.txt', 'r').readlines()
print(2)
for i in f:
    a[int(i.split()[0])-1] = a[int(i.split()[0])-1][:int(i.split()[1])-1] + '1' + a[int(i.split()[0])-1][int(i.split()[1]):]
print(3)
for i in range(len(a)):
    if '1001' in a[i]:
        print(i+1, a[i].index('1001') + 2)
