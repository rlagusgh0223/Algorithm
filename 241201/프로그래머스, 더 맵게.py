import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        x = heapq.heappop(scoville)
        # 제일 작은 값이 K 이상이어야 한다
        if x >= K:
            return answer
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x + 2*y)
        answer += 1
    return -1 if scoville[0]<K else answer

import sys

s = list(map(int, sys.stdin.readline().split(", ")))
k = int(sys.stdin.readline())
print(solution(s, k))