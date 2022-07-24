# 최소힙으로 구해야 하므로 -1을 곱할 필요 없다
import heapq, sys
N = int(sys.stdin.readline())
card = []
answer = 0
for i in range(N):
    card.append(int(sys.stdin.readline()))
heapq.heapify(card)

while len(card)>1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    sum = first+second
    answer += sum
    heapq.heappush(card, sum)

print(answer)