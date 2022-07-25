import heapq
N = int(input())
card = []
answer = 0
for i in range(N):
    card.append(int(input()))
heapq.heapify(card)

while len(card) > 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    Sum = first + second
    answer += Sum
    heapq.heappush(card, Sum)

print(answer)