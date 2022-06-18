dp = [0] * 10001    # dp 메모이제이션을 위한 배열 크기를 n의 최댓값+1로 설정
glass = [0] * 10001    # 포도주 양의 상태를 저장하기 위한 배열을 생성한다

n = int(input())    # n과 포도주 양의 상태를 입력받는다
for i in range(1, n+1):
  glass[i] = int(input())

dp[1] = glass[1]    # 첫번째 포도주 잔으로 설정한다
dp[2] = glass[1] + glass[2]    # 첫번째 + 두번째 포도주 잔으로 설정한다
for i in range(3, n+1):
  dp[i] = max(dp[i-1], dp[i-2]+glass[i], dp[i-3]+glass[i-1]+glass[i])

print(dp[n])