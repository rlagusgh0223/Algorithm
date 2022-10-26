import sys
N, K = map(int, sys.stdin.readline().split())
lst = [[0, 0]]
check = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = lst[i][0]
        value = lst[i][1]
        if j < weight:
            check[i][j] = check[i-1][j]
        else:
            check[i][j] = max(check[i-1][j-weight]+value, check[i-1][j])
print(check[N][K])