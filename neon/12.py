for i in range(1010101, 10000000):
    a = str(i)
    b = a
    while '00' not in a:
        try:
            if a != a.replace('01', '210', 1):
                a = a.replace('01', '210', 1)
            if a != a.replace('02', '3101', 1):
                a = a.replace('02', '3101', 1)
            if a != a.replace('02', '3101', 1):
                a = a.replace('03', '2012', 1)
        except:
            break

    if (a.count('1') == 61) and (a.count('2') == 50) and (a.count('3') == 18):
        print(b)


    a = '0' + str(i)
    b = a
    while '00' not in a:
        try:
            if a != a.replace('01', '210', 1):
                a = a.replace('01', '210', 1)
            if a != a.replace('02', '3101', 1):
                a = a.replace('02', '3101', 1)
            if a != a.replace('02', '3101', 1):
                a = a.replace('03', '2012', 1)
        except:
            break

    if (a.count('1') == 61) and (a.count('2') == 50) and (a.count('3') == 18):
        print(i)

    print(0000000000000)