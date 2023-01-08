import sys
K = int(sys.stdin.readline())
A = [0, 1] + [0]*(K-2)
B = [1, 1] + [0]*(K-2)
for i in range(2, K):
    A[i] = A[i-1] + A[i-2]
    B[i] = B[i-1] + B[i-2]
print(A[K-1], B[K-1])