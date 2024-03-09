import heapq


def solution(ability, number):
    answer = 0
    heapq.heapify(ability)
    for i in range(number):
        ab = 0
        ab += heapq.heappop(ability)
        ab += heapq.heappop(ability)
        heapq.heappush(ability, ab)
        heapq.heappush(ability, ab)
    answer = sum(ability)
    return answer

import sys

ability = list(map(int, sys.stdin.readline().split(", ")))
number = int(sys.stdin.readline())
print(solution(ability, number))