import heapq


def solution(ability, number):
    # heapify : 리스트를 heap으로 바꾸는 함수
    heapq.heapify(ability)

    # 가장 능력치가 작은 사원 2명의 능력을 더하고
    # 2사원의 능력을 더한 값으로 바꾼다
    for i in range(number):
        answer = heapq.heappop(ability) + heapq.heappop(ability)
        [heapq.heappush(ability, answer) for i in range(2)]
    
    return sum(ability)

import sys

ability = list(map(int, sys.stdin.readline().split(", ")))
number = int(sys.stdin.readline())
print(solution(ability, number))