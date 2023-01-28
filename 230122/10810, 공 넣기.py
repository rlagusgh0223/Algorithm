import sys
N, M = map(int, sys.stdin.readline().split())
lst = [0]*(N+1)
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for x in range(i, j+1):
        lst[x] = k
print(*lst[1:], sep=' ')