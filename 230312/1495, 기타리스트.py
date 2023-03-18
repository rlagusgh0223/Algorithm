import sys
N, S, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
music = [[0]*(M+1) for _ in range(N+1)]
music[0][S] = 1
ans = -1
for i in range(N):
    for j in range(M+1):
        if music[i][j] == 1:
            if j-lst[i] >= 0:
                music[i+1][j-lst[i]] = 1
            if j+lst[i] <= M:
                music[i+1][j+lst[i]] = 1
for i in range(M, -1, -1):
    if music[N][i] == 1:
        ans = i
        break
print(ans)