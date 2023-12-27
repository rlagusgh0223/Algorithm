def solution(d, budget):
    answer = 0
    d.sort()
    while answer<len(d) and budget-d[answer]>=0:
        budget -= d[answer]
        answer += 1
    return answer

import sys
d = list(map(int, sys.stdin.readline().split(",")))
budget = int(sys.stdin.readline())
print(solution(d, budget))