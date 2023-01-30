X, Y = [], []

for _ in range(3):
    A, B = map(int, input().split())
    X.append(A)
    Y.append(B)

for i in range(3):
    if X.count(X[i]) % 2 != 0 :
        A = X[i]
    if Y.count(Y[i]) % 2 != 0 :
        B = Y[i]

print(A, B)