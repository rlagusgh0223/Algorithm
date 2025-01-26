import heapq


def solution(operations):
    answer = []
    for op in operations:
        x, y = op.split()
        y = int(y)
        if x == 'I':
            heapq.heappush(answer, y)
        elif len(answer) > 0:
            if y == 1:
                answer.remove(max(answer))
            else:
                heapq.heappop(answer)

    return [max(answer), min(answer)] if answer else [0, 0]

import sys

print(solution(list(sys.stdin.readline().strip().split('", "'))))
