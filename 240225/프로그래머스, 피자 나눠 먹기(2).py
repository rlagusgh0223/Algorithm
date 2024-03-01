def solution(n):
    answer = 0
    while True:
        answer += 1
        if (6*answer) % n == 0:
            return answer

import sys

print(solution(int(sys.stdin.readline())))
