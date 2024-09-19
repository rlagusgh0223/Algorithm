def solution(myString):
    answer = [len(s) for s in myString.split('x')]
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
