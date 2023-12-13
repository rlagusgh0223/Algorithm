def solution(n):
    answer = 0
    n = str(n)
    for s in n:
        answer += int(s)
    return answer

import sys
n = int(sys.stdin.readline())
print(solution(n))