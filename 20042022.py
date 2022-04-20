f=sorted([int(l.strip()) for l in open('26_20.txt').readlines()[1:]])[::-1]
for i in range(len(f)):
    for j in range(len(f)):
        x = f[i]*f[j]
        if x%14==0 and i!=j:
            print(x); break
    else: continue
    break

f=sorted([int(l.strip()) for l in open('26_20_1.txt').readlines()[1:]])[::-1]
for i in range(len(f)):
    for j in range(len(f)):
        x = f[i]*f[j]
        if x%14==0 and i!=j:
            print(x); break
    else: continue
    break