for i in range(1000000):
    a = bin(i).replace('0b', '')
    b = 0
    c = 0
    for j in range(len(a)):
        if a[j] == '0' and (j+1)%2 == 1:
            b += 1
        if a[j] == '1' and (j+1)%2 == 0:
            c += 1
    
    if int(b) - int(c) == -5 or int(b) - int(c) == 5:
        print(i)
        break
