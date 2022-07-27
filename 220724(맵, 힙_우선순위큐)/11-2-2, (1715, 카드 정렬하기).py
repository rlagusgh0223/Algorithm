import heapq, sys
N = int(sys.stdin.readline())
card = []
answer = 0
for i in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(card, x)

while len(card) > 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    cardsum = first + second
    answer += cardsum
    heapq.heappush(card, cardsum)

print(answer)