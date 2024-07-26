def solution(number):
    answer = 0
    for n in number:
        answer += int(n)
    return answer % 9

import sys

print(solution(sys.stdin.readline().strip()))
