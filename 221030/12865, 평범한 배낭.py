import sys
N, K = map(int, sys.stdin.readline().split())
back = [[0, 0]]
check = [[0]*(K+1) for _ in range(N+1)]
for i in range(N):
    back.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, N+1):
    for j in range(i, K+1):
        weight = back[i][0]
        value = back[i][1]
        if j < weight:
            check[i][j] = check[i-1][j]
        else:
            check[i][j] = max(check[i-1][j-weight]+value, check[i-1][j])
print(check[N][K])