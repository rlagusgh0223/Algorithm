import sys
N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
C = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]
for i in range(N):
    print(' '.join(map(str, C[i])))