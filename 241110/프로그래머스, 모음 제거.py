def solution(my_string):
    answer = ''
    for s in my_string:
        if s not in ['a', 'e', 'i', 'o', 'u']:
            answer += s
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
