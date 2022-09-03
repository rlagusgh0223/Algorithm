n, k = map(int, input().split())
dp = [[0]*1001 for _ in range(1001)]  # 메모이제이션을 위한 배열 생성, 크기는 n,k의 최댓값 1000

for i in range(1, n+1):  # 1~n의 범위 탐색
    for j in range(i+1):  # 1~i까지 k의 범위를 탐색하기 위한 반복문(k를 j로 쓴 것 같다)
        if j == 0:  # k가 0이면 어차피 전부 1
            dp[i][j] = 1
        elif j == i:  # k가 n이면 전부 1
            dp[i][j] = 1
        else:  # 나머지는 구한값 % 10007
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007

print(dp[n][k])