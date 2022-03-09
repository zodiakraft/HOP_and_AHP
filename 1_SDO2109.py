file = open('26.txt', 'r')
first, second = map(int, file.readline().split())
l1st = []

for i in range(second):
    l1st.append(int(file.readline()))

l1st.sort()
index = 0

for i in range(second):
    if index + l1st[i] <= first:
        index = index + l1st[i]
        last_index = i

last = l1st[last_index]
index = index - last

for i in range(last_index + 1, second):
    if index + l1st[i] <= first:
        last = l1st[i]

print(last_index + 1, last)