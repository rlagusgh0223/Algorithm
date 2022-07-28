import sys, heapq
N = int(sys.stdin.readline())
card = []
answer = 0
for _ in range(N):
    card.append(int(sys.stdin.readline()))
heapq.heapify(card)

while len(card) > 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    csum = first + second
    answer += csum
    heapq.heappush(card, csum)

print(answer)