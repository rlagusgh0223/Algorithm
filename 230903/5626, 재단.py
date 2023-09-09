# 어떻게 해도 답이 안나옴

# import sys
# N = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))

# # dp 테이블 선언
# # dp[i][j] = i번째 열까지 높이가 j로 끝나는 경우의 수
# dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
# dp[0][0] = 1

# # i번째 열까지 높이가 j로 끝나는 경우의 수를 계산
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         # 이전 열의 높이와 같으면
#         if arr[i-1] == j:
#             dp[i][j] += dp[i-1][j-1] + dp[i-1][j]
#         # 이전 열의 높이보다 1 높으면
#         elif arr[i-1] == j-1:
#             dp[i][j] += dp[i-1][j-1]

# # 남은 제단의 높이와 일치하는 경우의 수 출력
# print(dp[N][arr[-1]])




# n = 기둥 수
# arr = 기둥 높이 목록
n, arr = int(input()), list(map(int, input().split()))

# dp[i][j] = i번째 열까지 높이가 j로 끝나는 경우의 수
# i = 열 번호
# j = 높이
dp = [[0 for _ in range(n + 1)] for _ in range(2)]
dp[0][0] = 1
dp[1][0] = 1

# 기둥의 높이가 양끝까지 도달할 수 있는 최대 높이 계산
for i in range(1, n + 1):
    arr[i - 1] = min(i, n - i)

# i번째 열까지 높이가 j로 끝나는 경우의 수를 계산
for i in range(1, n + 1):
    idx = i % 2  # i번째 열을 i%2로 생각하고 노드 값을 줄였다
    pre = (idx + 1) % 2  # 바로 앞 제단
    for x in range(len(arr)//2):  # dp[idx] 비우고 시작
        dp[idx][x] = 0

    # i번째 기둥이 -1이면, 높이 0에서 시작하여 기둥의 양끝까지 도달할 수 있는 모든 높이가 가능
    if arr[i - 1] == -1:
        for x in range(len(arr)//2):
            if x > min(i, (n-1)-i):  # 가능한 최대 높이까지만
                break
            for k in range(-1, 2):
                prex = x + k
                if prex < 0:  # 음수 높이 불가능
                    continue
                dp[idx][x] += dp[pre][prex]
                dp[idx][x] %= 1000000007

    # i번째 기둥이 특정 높이로 표시되어 있으면, 이전 기둥에서 그 높이로 도달할 수 있는 방법의 수를 추가
    else:
        for k in range(-1, 2):
            prex = arr[i-1] + k
            if prex < 0:
                continue
            dp[idx][arr[i - 1]] += dp[pre][arr[i - 1] + k]
            dp[idx][arr[i - 1]] %= 1000000007

# 마지막 열에서 높이 0에 도달할 수 있는 방법의 수 출력
print(dp[idx][0])