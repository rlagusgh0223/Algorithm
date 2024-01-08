def solution(n, m, section):
    answer = 0
    now = 0
    for s in section:
        if now < s:
            answer += 1
            now = s + m - 1
    return answer

import sys
n, m = map(int, sys.stdin.readline().split())
sec = list(map(int, sys.stdin.readline().split(", ")))
print(solution(n, m, sec))