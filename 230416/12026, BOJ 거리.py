import sys
N = int(sys.stdin.readline())
block = list(sys.stdin.readline().rstrip())
ck = sys.maxsize
dp = [ck]*N
dp[0] = 0
for i in range(1, N):
    for j in range(i):
        if block[j]=='B' and block[i]=='O':
            dp[i] = min(dp[i], dp[j]+(i-j)**2)
        elif block[j]=='O' and block[i]=='J':
            dp[i] = min(dp[i], dp[j]+(i-j)**2)
        elif block[j]=='J' and block[i]=='B':
            dp[i] = min(dp[i], dp[j]+(i-j)**2)
if dp[-1] == ck:
    print(-1)
else:
    print(dp[-1])