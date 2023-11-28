import heapq
def solution(operations):
    answer = []
    for op in operations:
        o, p = op.split()
        p = int(p)
        if o == 'I':
            heapq.heappush(answer, p)
        elif len(answer)>0 and o=='D':
            if p == 1:
                maxop = max(answer)
                answer.remove(maxop)
            elif p == -1:
                heapq.heappop(answer)
    if len(answer) == 0:
        return [0, 0]
    return [max(answer), min(answer)]

import sys
op = list(sys.stdin.readline().strip().split('", "'))
print(solution(op))