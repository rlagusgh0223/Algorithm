def solution(s1, s2):
    answer = 0
    for s in s1:
        if s in s2:
            answer += 1
    return answer

import sys

s1 = list(sys.stdin.readline().strip().split('", "'))
s2 = list(sys.stdin.readline().strip().split('", "'))
print(solution(s1, s2))