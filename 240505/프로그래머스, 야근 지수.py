import heapq


def solution(n, works):
    # 남은 작업시간보다 일이 적으면 일을 다 할 수 있으므로 피로도는 없다
    if n >= sum(works):
        return 0
    
    # heappop은 가장 작은 수를 반환하므로 -를 붙여서 가장 큰 수가 나오게 한다
    works = [-w for w in works]
    # heapify : 리스트를 heap 자료형으로 만들어준다
    heapq.heapify(works)
    for i in range(n):
        # works에서 가장 작은 값(-1 * 가장 큰값이 들어있다) pop연산
        work = heapq.heappop(works)
        # 작업량이 1시간어치 줄었지만 -1을 곱한값을 넣었으므로 1을 더해서 작업량을 없앤다
        heapq.heappush(works, work+1)

    return sum([w**2 for w in works])

import sys

works = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(n, works))