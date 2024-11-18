def solution(my_string):
    answer = []
    for ms in my_string:
        if ms not in answer:
            answer.append(ms)
    return ''.join(answer)

import sys

print(solution(sys.stdin.readline().strip()))
