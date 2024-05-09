def solution(s):
    answer = 1
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            ck = s[i:j]
            if ck == ck[::-1]:
                answer = max(answer, len(ck))
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
