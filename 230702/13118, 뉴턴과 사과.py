import sys
lst = list(map(int, sys.stdin.readline().split()))
x, y, r = map(int, sys.stdin.readline().split())
if x in lst:
    print(lst.index(x) + 1)
else:
    print(0)