import heapq, sys
N = int(sys.stdin.readline())
hp = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(hp, -x)
    else:
        if hp:
            print(-1 * heapq.heappop(hp))
        else:
            print(0)