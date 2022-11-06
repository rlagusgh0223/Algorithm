def next_per(a):
    i = len(a) - 1
    while i>0 and a[i-1] >= a[i]:
        i -= 1
    while i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

import sys
N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
d = list(range(N))
ans = sys.maxsize
while True:
    ok = True
    s = 0
    for i in range(N-1):
        if W[d[i]][d[i+1]]==0:
            ok = False
            break
        else:
            s += W[d[i]][d[i+1]]
    if ok and W[d[-1]][d[0]] != 0:
        s += W[d[-1]][d[0]]
        ans = min(ans, s)
    if not next_per(d):
        break
    if d[0] != 0:
        break
print(ans)