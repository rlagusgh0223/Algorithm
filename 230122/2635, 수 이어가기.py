def number(N, i):
    lst = [N, N-i]
    cnt = 2
    while lst[cnt-2] - lst[cnt-1] >= 0:
        lst.append(lst[cnt-2] - lst[cnt-1])
        cnt += 1
    return lst

import sys
N = int(sys.stdin.readline())
ans, ck = 0, 0
for i in range(1, N):
    lst = number(N, i)
    if ans < len(lst):
        ans = len(lst)
        ck = i
lst = number(N, ck)
print(len(lst))
print(*lst, sep=' ')