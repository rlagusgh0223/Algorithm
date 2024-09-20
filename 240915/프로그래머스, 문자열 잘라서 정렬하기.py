def solution(myString):
    answer = sorted([myStr for myStr in myString.split('x') if myStr])
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
