def solution(s):
    answer = 0
    s = list(s.split())
    for i in range(len(s)):
        if s[i] == 'Z':
            answer -= int(s[i-1])
        else:
            answer += int(s[i])
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
