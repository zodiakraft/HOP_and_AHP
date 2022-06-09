a = 0
n = 0
for i in range(11000000, 999999999):
    b = i - 1
    while b > 0:
        if i % b == 0 and n < 2:
            a+=b
            n+=1
        elif n == 2:
            break
        b -= 1
    if a > 0 and n == 2 and a<10000: print(a)
    a = 0
    n = 0
