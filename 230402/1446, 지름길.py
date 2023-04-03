# 한 칸 전 위치의 테이블값 + 1이 현재 테이블 값보다 작다면 현재 테이블 값 수정
# 현재 위치에 지름길이 있다면 지름길로 건너간 곳의 원래 테이블 값과 지금 테이블+지름길 거리 중 작은것으로 한다
import sys
N, D = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        dp[i] = min(dp[i-1]+1, dp[i])
    for start, end, length in lst:
        if i==start and end<=D:
            dp[end] = min(dp[i]+length, dp[end])
print(dp[D])