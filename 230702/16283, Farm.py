import sys
a, b, n, w = map(int, sys.stdin.readline().split())
lst = []
for i in range(1, n):
    if i*a + (n-i)*b == w:
        lst.append([i, n-i])
if len(lst) == 1:
    print(*lst[0])
else:
    print(-1)