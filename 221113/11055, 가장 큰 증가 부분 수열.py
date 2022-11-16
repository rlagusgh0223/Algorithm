import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
D = [0] * N
for i in range(N):
    D[i] = A[i]
    for j in range(i):
        if A[j] < A[i] and D[i] < D[j]+A[i]:
            D[i] = D[j] + A[i]
print(max(D))