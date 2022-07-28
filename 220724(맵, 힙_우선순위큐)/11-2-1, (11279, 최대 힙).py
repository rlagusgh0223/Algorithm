import sys, heapq
N = int(sys.stdin.readline())
number = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if number:
            print(-1 * heapq.heappop(number))
        else:
            print(0)
    else:
        heapq.heappush(number, -x)