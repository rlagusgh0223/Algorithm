n, m = map(int, input().split())
A = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j, now in enumerate(list(map(int, list(input())))):
        A[i][j+1] = now
DP = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i][j]:
            DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
print(max([max(i) for i in DP]) ** 2)