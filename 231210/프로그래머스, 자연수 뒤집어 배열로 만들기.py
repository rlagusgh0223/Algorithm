def solution(n):
    answer = list(str(n))
    answer = list(map(int, answer[::-1]))
    return answer

import sys
n = int(sys.stdin.readline())
print(solution(n))