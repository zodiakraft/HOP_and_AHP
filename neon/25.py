for i in range(X, X_1):
    [n:= k + i // k for k in range(2, i) if i % k == 0]
if n % X_2 == X_3: print(i, n)