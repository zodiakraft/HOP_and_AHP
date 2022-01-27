start = 1633046400
end = start + 30 * 24 * 3600
start_week = 1634515200
end_week = start_week + 7 * 24 * 3600

file = open('26.txt', 'r')
lines = file.readlines()
n = 0
A = [0] * (end_week - start_week)

for i in range(1, len(lines)):
    if (lines[i].split()[0] == lines[i].split()[1]) and (lines[i].split()[0] == '0'):
        #n += 1
        A[:]=[i+1 for i in A]
    if (int(lines[i].split()[0]) == int(lines[i].split()[1])) and (lines[i].split()[1] >= start_week and lines[i].split()[1] <= end_week):
        A[int(lines[i].split()[0]) - start_week] += 1 #maybe -1
    if (int(lines[i].split()[0]) > start) and (int(lines[i].split()[1]) <= end):
        pass
    if (lines[i].split()[0] == '0') and (lines[i].split()[1] <= end):
        pass


print(end)
print(max(A))
file.close()
#7768 20
