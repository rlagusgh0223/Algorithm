N, M = map(int, input().split())
a = [[False]*(N+1) for _ in range(N+1)]
degree = [0] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    a[A][B] = a[B][A] = True
    degree[A] += 1
    degree[B] += 1
ans = -1
for i in range(1, N+1):
    for j in range(1, N+1):
        if a[i][j]:
            for k in range(1, N+1):
                if a[i][k] and a[j][k]:
                    s = degree[i] + degree[j] + degree[k] - 6
                    if ans==-1 or ans>s:
                        ans = s
print(ans)