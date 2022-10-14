import sys
import heapq

N = int(sys.stdin.readline())
leftHeap = []
rightHeap = []
answer = []

for i in range(N):
    now = int(sys.stdin.readline())
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -now)
    else:
        heapq.heappush(rightHeap, now)
    if rightHeap and -leftHeap[0] > rightHeap[0]:
        left = heapq.heappop(leftHeap)
        right = heapq.heappop(rightHeap)
        heapq.heappush(leftHeap, -right)
        heapq.heappush(rightHeap, -left)
    answer.append(-leftHeap[0])

for num in answer:
    print(num)