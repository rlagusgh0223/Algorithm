import heapq
from copy import deepcopy

K, N = map(int, input().split())
p_list = list(map(int, input().split()))
lst = deepcopy(p_list)
ck = set()
heapq.heapify(lst)
ith = 0

while ith < N:
    mn = heapq.heappop(lst)
    if mn in ck:
        continue
    ith += 1
    ck.add(mn)
    for i in p_list:
        if mn*i < 2**31:
            heapq.heappush(lst, mn*i)

print(mn)