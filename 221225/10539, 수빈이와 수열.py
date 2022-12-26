import sys
N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A = [0] * N
A[0] = B[0]
for i in range(1, N):
    A[i] = B[i]*(i+1) - sum(A)
print(*A, sep=' ')