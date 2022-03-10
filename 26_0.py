file = open('26.txt', 'r')
l1st = list(map(int,file.read().split()))
first, second = l1st.pop(0), l1st.pop(0)
l1st.sort()
index = 0

for i in range(second):
    index += l1st[i]
    if index > first:
        break

index -= l1st[i] + l1st[i-1]
index_1 = first - index
left = i
right = second

while right - left > 1:
    ariphm = (right + left) // 2
    if l1st[ariphm] > index_1:
        right = ariphm
    else:
        left = ariphm

print(i, l1st[left])