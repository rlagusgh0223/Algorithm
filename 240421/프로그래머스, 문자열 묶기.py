def solution(strArr):
    answer = [0] * 31
    for sA in strArr:
        answer[len(sA)] += 1
    return max(answer)

import sys

strArr = list(sys.stdin.readline().strip().split('","'))
print(solution(strArr))