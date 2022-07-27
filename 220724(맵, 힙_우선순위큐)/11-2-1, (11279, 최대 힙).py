import heapq, sys
N = int(sys.stdin.readline())
heap = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)