def solution(num_str):
    answer = 0
    for num in num_str:
        answer += int(num)
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
