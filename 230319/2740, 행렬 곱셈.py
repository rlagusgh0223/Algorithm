import sys
N, M = map(int, sys.stdin.readline().split())
A = [[] for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, sys.stdin.readline().split()))
M, K = map(int, sys.stdin.readline().split())
B = [[] for _ in range(M)]
for i in range(M):
    B[i] = list(map(int, sys.stdin.readline().split()))

ans = [[0]*K for _ in range(N)]
for i in range(N):
    for k in range(K):
        for j in range(M):
            ans[i][k] += A[i][j] * B[j][k]
for i in range(N):
    print(*ans[i])