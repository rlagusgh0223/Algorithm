# 매번 우선순위 큐를 적용해서 작은값끼리 더해지도록 한다
import sys, heapq
N = int(sys.stdin.readline())
card = []
answer = 0
for i in range(N):
    heapq.heappush(card, int(sys.stdin.readline()))

while len(card)>1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    answer += (first+second)
    heapq.heappush(card, first+second)

print(answer)