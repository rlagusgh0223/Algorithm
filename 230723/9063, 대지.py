import sys
nx, mx, ny, my = 10001, -10001, 10001, -10001
N = int(sys.stdin.readline())
X = [0] * N
Y = [0] * N
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    X[i] = x
    Y[i] = y
print((max(X) - min(X)) * (max(Y) - min(Y)))