import sys
N, M = map(int, sys.stdin.readline().split())
backet = [int(x) for x in range(N+1)]
for i in range(M):
    i, j = map(int, sys.stdin.readline().split())
    backet[i:j+1] = backet[j:i-1:-1]
print(*backet[1:])