n = int(input())
DP = [[0]*(n+1) for _ in range(n+1)]
A = [[0] for _ in range(n+1)]
for i in range(1, n+1):
    A[i] += list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(1, len(A[i])):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j])+A[i][j]
print(max(DP[-1]))