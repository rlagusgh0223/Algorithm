import heapq


def solution(operations):
    answer = []
    for op in operations:
        o, p = op.split()
        p = int(p)
        if o == 'I':
            heapq.heappush(answer, p)
        elif o=='D' and len(answer)>0:
            if p == 1:
                # heapq는 최솟값만 제거할 수 있고
                # 최댓값을 제거하는 기능은 없으므로
                # 그냥 직접 제거한다
                answer.remove(max(answer))
            else:
                heapq.heappop(answer)
    
    if len(answer) == 0:
        return [0, 0]
    return [max(answer), min(answer)]


import sys

print(solution(list(sys.stdin.readline().strip().split('", "'))))
