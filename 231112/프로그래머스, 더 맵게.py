import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # 리스트를 heap으로 변환
    x = heapq.heappop(scoville)
    while x < K:
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x + (y*2))
        answer += 1
        x = heapq.heappop(scoville)
        if len(scoville)==0 and x < K:
            return -1
    return answer


import sys
scoville = list(map(int, sys.stdin.readline().strip().split(", ")))
K = int(sys.stdin.readline())
print(solution(scoville, K))