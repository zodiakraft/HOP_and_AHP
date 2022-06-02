a = [int(i) for i in input().split()]
min_index = a.index(min(a))
max_index = a.index(max(a))
[a[max_index], a[min_index]] = [a[min_index], a[max_index]]
print(' '.join([str(i) for i in a]))