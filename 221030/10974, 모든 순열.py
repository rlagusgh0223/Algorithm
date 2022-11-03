def next_per(lst):
    i = len(lst) - 1
    while i>0 and lst[i-1]>=lst[i]:
        i -= 1
    if i<=0:
        return False
    j = len(lst) - 1
    while lst[j] <= lst[i-1]:
        j -= 1
    lst[i-1], lst[j] = lst[j], lst[i-1]
    j = len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return True

import sys
N = int(sys.stdin.readline())
lst = [int(x) for x in range(1, N+1)]
print(' '.join(map(str, lst)))
while True:
    if next_per(lst):
        print(' '.join(map(str, lst)))
    else:
        break