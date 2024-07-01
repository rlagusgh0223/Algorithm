def solution(a, d, included):
    answer = 0
    for now in included:
        if now:
            answer += a
        a += d
    return answer

import sys

a, d = map(int, sys.stdin.readline().split())
included = sys.stdin.readline().strip().split(", ")
included = [s.lower()=='true' for s in included]
print(solution(a, d, included))