def solution(my_string):
    answer = []
    for ms in my_string:
        if ms.isdigit():
        # if ms in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            answer.append(int(ms))
    return sorted(answer)

import sys

print(solution(sys.stdin.readline().strip()))
