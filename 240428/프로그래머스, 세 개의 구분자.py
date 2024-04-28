def solution(myStr):
    answer = myStr.replace('a', ' ')
    answer = answer.replace('b', ' ')
    answer = answer.replace('c', ' ')
    answer = list(answer.split())
    if len(answer) == 0:
        return ["EMPTY"]
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
