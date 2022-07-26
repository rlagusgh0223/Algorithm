import heapq, sys
N = int(sys.stdin.readline())
number = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
       heapq.heappush(number, -x)
    else:
        if number:
            print(-1 * heapq.heappop(number))
        else:
            print(0)