p = []

for q in ('РОСОМАХА'):
    for w in ('РОСОМАХА'):
        for e in ('РОСОМАХА'):
            for r in ('РОСОМАХА'):
                for t in ('РОСОМАХА'):
                    for y in ('РОСОМАХА'):
                        for u in ('РОСОМАХА'):
                            for i in ('РОСОМАХА'):
                                o = q+w+e+r+t+y+u+i
                                if (o[0] != o[1]) and ((o[0] not in 'РСМХ') or (o[1] not in 'РСМХ')) and ((o[0] not in 'ОА') or (o[1] not in 'ОА')) and (o[1] != o[2]) and ((o[1] not in 'РСМХ') or (o[2] not in 'РСМХ')) and ((o[1] not in 'ОА') or (o[2] not in 'ОА')) and (o[2] != o[3]) and ((o[2] not in 'РСМХ') or (o[3] not in 'РСМХ')) and ((o[2] not in 'ОА') or (o[3] not in 'ОА')) and (o[3] != o[4]) and ((o[3] not in 'РСМХ') or (o[4] not in 'РСМХ')) and ((o[3] not in 'ОА') or (o[4] not in 'ОА')) and (o[4] != o[5]) and ((o[4] not in 'РСМХ') or (o[5] not in 'РСМХ')) and ((o[4] not in 'ОА') or (o[5] not in 'ОА')) and (o[5] != o[6]) and ((o[5] not in 'РСМХ') or (o[6] not in 'РСМХ')) and ((o[5] not in 'ОА') or (o[6] not in 'ОА')) and (o[6] != o[7]) and ((o[6] not in 'РСМХ') or (o[7] not in 'РСМХ')) and ((o[6] not in 'ОА') or (o[7] not in 'ОА')) and ('Р' in o) and ('С' in o) and ('М' in o) and ('Х' in o) and (o.count('А') == 2) and (o.count('О') == 2):
                                    p.append(o)

print (len(list(set(p))))