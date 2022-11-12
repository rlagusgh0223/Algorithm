import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
D = [0] * n
D[0] = A[0]
for i in range(1, n):
    D[i] = max(A[i], D[i-1]+A[i])
print(max(D))