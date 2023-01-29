import sys
N = int(sys.stdin.readline())
f = list(map(int, sys.stdin.readline().split()))
dp = [0] * N
dp[N-1] = 1  # 마지막 칸은 점프대가 있든 없든 무조건 1칸 이동이다
for i in range(N-2, -1, -1):
    if f[i] == 0:
        dp[i] = dp[i+1] + 1
    else:
        if i+f[i]+1 >= N:
            dp[i] = 1
        else:
            dp[i] = dp[i+f[i]+1]+1
print(*dp, sep=' ')