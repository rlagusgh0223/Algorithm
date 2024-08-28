import heapq


def solution(operations):
    answer = []
    for op in operations:
        o, p = op.split()
        p = int(p)
        if o == 'I':
            heapq.heappush(answer, p)
        elif len(answer) > 0:
            if p == 1:
                answer.remove(max(answer))
            else:
                heapq.heappop(answer)
    if answer:
        return [max(answer), min(answer)]
    return [0, 0]

import sys

operations = list(sys.stdin.readline().strip().split('", "'))
print(solution(operations))