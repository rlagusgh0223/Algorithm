# '시간'이라는 범위를 기준으로 답을 좁혀가며
# 탐색하는 구조기 때문에 이분탐색 문제로 분류
def solution(n, times):
    answer = 0
    l, r = min(times), max(times)*n
    while l <= r:
        mid = (l + r) // 2
        # mid 시간동안 점검 가능한 사람의 수
        people = sum(mid//time for time in times)
        if people >= n:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    return answer

import sys

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split(", ")))
print(solution(n, times))