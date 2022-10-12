# 힙을 사용하지 않으면 시간초과 난다
import sys
import heapq
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not lst:
            print('0')
        else:
            print(heapq.heappop(lst))
    elif x > 0:
        heapq.heappush(lst, x)