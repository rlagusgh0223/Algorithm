import sys
N, M = map(int, sys.stdin.readline().split())
b = [int(i) for i in range(N+1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    b[i], b[j] = b[j], b[i]
print(*b[1:], sep=' ')