#           A   C   A   D   A
#     0     0   0   0   0   0
# E   0     0   0   0   0   0
# C   0     0   1   0   0   0
# A   0     1   0   2   0   1
# D   0     0   0   0   3   0
# A   0     1   0   1   0   4


import sys
str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()
dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        # 두 문자열의 문자를 하나씩 비교하다가 같은 문자가 나오면
        if str1[i-1] == str2[j-1]:
            # (str1의 이전문자, str2의 이전문자 까지의 문자열 길이) + 1 을 입력한다
            dp[i][j] = dp[i-1][j-1] + 1
print(max(map(max, dp)))