# 가장 긴 감소하는 부분수열과 같은 알고리즘이라고 생각하면 된다
import sys
n = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
d.reverse()    # 리스트의 배열을 반대로 바꿔주는 함수
dp = [1] * n    # 그 자체로도 하나의 길이는 되니까 1로 초기화

# 가장 긴 감소하는 부분수열 알고리즘
for i in range(n):
    for j in range(i):
        if d[j] < d[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 수열의 길이에서 가장 긴 감소하는 부분수열의 길이를 빼면 제외해야 하는 병사의 수가 나온다
print(n - max(dp))