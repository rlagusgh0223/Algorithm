import sys
N, M = map(int, sys.stdin.readline().split())
backet = list(range(N+1))
for i in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    backet[i:j+1] = backet[k:j+1] + backet[i:k]
print(*backet[1:])