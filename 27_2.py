f = open('27991_A.txt', 'r')
X = f.readlines()

MAX17=[0, 0]
MAX=[0, 0]

for i in X:
    if int(i)%17==0 and int(i)%2==0 and int(i)>MAX17[0]:
        MAX17[0]=int(i)
    if int(i)%17==0 and int(i)%2==1 and int(i)>MAX17[1]:
        MAX17[1]=int(i)
    if int(i)%17==0 and int(i)%2==0 and int(i)>MAX[0]:
        MAX[0]=int(i)
    if int(i)%17==0 and int(i)%2==1 and int(i)>MAX[1]:
        MAX[1]=int(i)

print(MAX17[0], MAX17[1], MAX17[0]+MAX17[1])
print(MAX[0], MAX17[1], MAX[0]+MAX17[1])
print(MAX17[0], MAX[1], MAX17[0]+MAX[1])
# 3077 8759