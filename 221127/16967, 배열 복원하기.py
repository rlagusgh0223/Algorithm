import sys
H, W, X, Y = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(H+X)]
for i in range(H):
    for j in range(W):
        A[i+X][j+Y] -= A[i][j]
for i in range(H):
    print(*A[i][:W])