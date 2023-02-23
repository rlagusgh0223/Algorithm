# dp[i-1]에서 2x1 타일을 세로로 한개 붙이는 경우 : 1
# dp[i-2]에서 2x1 타일을 가로로 두개 붙이는 경우, 2x2 타일을 한개 붙이는 경우 : 2
# 문제에서 n을 0도 줄 수 있기 때문에 0을 입력할 경우도 dp에 넣어야 한다
import sys
dp = [0] * 251
dp[0], dp[1], dp[2] = 1, 1, 3
for i in range(3, 251):
    dp[i] = dp[i-1] + 2*dp[i-2]
try:
    while True:
        n = int(sys.stdin.readline())
        print(dp[n])
except:
    exit()