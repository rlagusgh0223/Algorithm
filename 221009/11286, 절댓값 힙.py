import sys
import heapq

# 힙큐에 값을 넣을때 (절대값, 원래값) 쌍으로 넣어줌으로써
# 절대값을 기준으로 정렬을 할 수 있다
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(lst, (abs(x), x))
    else:
        if not lst:
            print('0')
        else:
            print(heapq.heappop(lst)[1])