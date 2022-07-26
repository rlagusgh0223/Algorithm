import heapq, sys
N = int(sys.stdin.readline())
number = []
answer = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(number, num)
while len(number)>1:
    first = heapq.heappop(number)
    second = heapq.heappop(number)
    plus = first+second
    answer += plus
    heapq.heappush(number, plus)

print(answer)