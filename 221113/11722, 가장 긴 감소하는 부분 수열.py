import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
D = [1] * N
for i in range(N):
    for j in range(i):  # 0~i-1까지의 수와 비교
        if A[i] < A[j] and D[i] < D[j] + 1:
            D[i] = D[j] + 1
print(max(D))