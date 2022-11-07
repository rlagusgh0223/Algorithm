import sys
N, M = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
ans = 0
for s in range(1<<N*M):
    sum = 0
    for i in range(N):
        cur = 0
        for j in range(M):
            k = i*M + j
            if (s&(1<<k)) == 0:
                cur = cur*10 + a[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    for j in range(M):
        cur = 0
        for i in range(N):
            k = i*M + j
            if (s&(1<<k)) != 0:
                cur = cur*10 + a[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    ans = max(ans, sum)
print(ans)