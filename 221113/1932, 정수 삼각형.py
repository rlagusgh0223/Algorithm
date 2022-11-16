import sys
n = int(sys.stdin.readline())
A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))
D = [[0]*n for _ in range(n)]
D[0][0] = A[0][0]
for i in range(1, n):
    for j in range(i+1):
        D[i][j] = D[i-1][j] + A[i][j]
        if j-1>=0 and D[i][j] < D[i-1][j-1] + A[i][j]:
            D[i][j] = D[i-1][j-1] + A[i][j]
print(max(D[n-1]))