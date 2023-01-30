import sys
n = int(sys.stdin.readline())
dp = [0, 1]+[0]*(n-1)
for i in range(2, n+1):
    ans = 50000
    j = 1
    while j**2 <= i:
        # 지금 위치로부터 1**2, 2**2, 3**2순으로 앞의 수를 비교해 본다.
        # 찾은 자리에서 그 제곱수를 한번 더해주면 지금 값이 나온다
        ans = min(ans, dp[i-(j**2)])  
        j += 1
    dp[i] = ans + 1
print(dp[n])