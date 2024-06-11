# n명의 사람을 심사하기 위한 시간 구하기
def solution(n, times):
    answer = 0
    l, r = min(times), max(times)*n  # 가능한 최소시간과 최대시간
    while l <= r:
        mid = (l+r) // 2  # 가능한지 확인해볼 시간
        people = 0  # 현재 시간으로 점검할 사람
        for time in times:
            people += mid // time  # 현재 시간으로 이번 심사대에서 점검하는 사람
            if people >= n:
                break
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