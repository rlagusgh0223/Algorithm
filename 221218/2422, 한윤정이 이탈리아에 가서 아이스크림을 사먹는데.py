N, M = map(int, input().split())
a = [[False]*N for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    a[x-1][y-1] = a[y-1][x-1] = True
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if a[i][j] or a[j][k] or a[k][i]:
                continue
            ans += 1
print(ans)