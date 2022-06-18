dp = [0] * 1001    # dp메모이제이션을 위한 배열 크기를 n의 최댓값+1로 설정

n = int(input())    # n과 배열 arr을 입력받고, a[0]에 0을 삽입(a[1]~a[n]까지 수열을 받게 된다)
arr = list(map(int, input().split()))
arr.insert(0, 0)

answer = 0    # 정답을 저장하기 위한 answer변수 생성
for i in range(1, n+1):    # 점화식을 위한 이중 for문 사용
  for j in range(0, i):
    if arr[j]<arr[i]:    # 현재 수열값보다 작은 수가 있다면
      dp[i] = max(dp[i], dp[j]+1)    # dp[i]의 값을 현재 dp[i]의 값과 작은 수에 해당하는 dp[j]의 값+1 둘 중 큰것으로 한다
  answer = max(answer, dp[i])

print(answer)