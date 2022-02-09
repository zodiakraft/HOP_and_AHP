print('X Y Z W F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if int((x == (not(y) or z)) and (w or (x ==y))) == 1:
                    print(x, y, z, w, int((x == (not(y) or z)) and (w or (x ==y))))