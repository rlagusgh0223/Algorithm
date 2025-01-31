def solution(n, times):
    start, end = min(times), max(times)*n
    while start <= end:
        mid = (start + end) // 2
        people = sum(mid//t for t in times)
        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

import sys

n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split(", ")))
print(solution(n, t))