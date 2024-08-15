def solution(n, times):
    l, r = min(times), max(times)*n
    while l <= r:
        mid = (l+r) // 2
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