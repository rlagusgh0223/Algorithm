import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        x = heapq.heappop(scoville)
        if x >= K:
            return answer
        answer += 1
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x + 2*y)
    return -1 if scoville[0]<K else answer

import sys

s = list(map(int, sys.stdin.readline().split(", ")))
k = int(sys.stdin.readline())
print(solution(s, k))