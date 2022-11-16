import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d1 = [0] * n
d2 = [0] * n
for i in range(n):
    d1[i] = a[i]
    if i == 0:
        continue
    if d1[i] < d1[i-1] + a[i]:
        d1[i] = d1[i-1] + a[i]
for i in range(n-1, -1, -1):
    d2[i] = a[i]
    if i == n-1:
        continue
    if d2[i] < d2[i+1] + a[i]:
        d2[i] = d2[i+1] + a[i]
ans = max(d1)
for i in range(1, n-1):
    if ans < d1[i-1] + d2[i+1]:
        ans = d1[i-1] + d2[i+1]
print(ans)