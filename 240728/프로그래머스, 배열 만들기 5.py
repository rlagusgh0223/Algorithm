def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        result = int(intStr[s:s+l])
        if result > k:
            answer.append(result)
    return answer

import sys

intStrs = list(sys.stdin.readline().strip().split('","'))
k, s, l = map(int, sys.stdin.readline().split())
print(solution(intStrs, k, s, l))