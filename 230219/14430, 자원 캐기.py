import sys
N, M = map(int, sys.stdin.readline().split())
lst = [[0 for _ in range(M+1)]] + [[0]+list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(1, N+1):
    for j in range(1, M+1):
        lst[i][j] += max(lst[i-1][j], lst[i][j-1])
print(max(map(max, lst)))