def solution(my_string):
    answer = 0
    for ms in my_string:
        if ms.isdigit():
            answer += int(ms)
    return answer

import sys

print(solution(sys.stdin.readline()))
