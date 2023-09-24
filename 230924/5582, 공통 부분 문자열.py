#           A   C   A   D   A
#     0     0   0   0   0   0
# E   0     0   0   0   0   0
# C   0     0   1   0   0   0
# A   0     1   0   2   0   1
# D   0     0   0   0   3   0
# A   0     1   0   1   0   4

# pypy3로 해야된다
import sys
str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()
dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
ans = 0
for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        # 두 문자열의 문자를 하나씩 비교하다가 같은 문자가 나오면
        if str1[i-1] == str2[j-1]:
            # (str1의 이전문자, str2의 이전문자 까지의 문자열 길이) + 1 을 입력한다
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])
print(ans)

# map을 이용하면 2차원 배열의 최댓값을 한번에 구할 수 있지만, 메모리 초과가 나오는것같다
# print(max(map(max, dp)))