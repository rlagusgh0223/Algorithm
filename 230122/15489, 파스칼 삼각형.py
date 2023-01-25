import sys
R, C, W = map(int, sys.stdin.readline().split())
t = [[1]*i for i in range(1, 31)]
for i in range(2, 30):
    for j in range(1, i):
        t[i][j] = t[i-1][j-1] + t[i-1][j]
cnt = ans = 0
for i in range(R-1, R+W-1):
    for j in range(C-1, C+cnt):
        ans += t[i][j]
    cnt += 1
print(ans)