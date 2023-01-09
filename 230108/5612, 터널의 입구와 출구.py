import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
lst = [m]+[0]*n
for i in range(1, n+1):
    x, y = map(int, input().split())
    lst[i] = lst[i-1] + x - y
if min(lst) < 0:
    print(0)
else:
    print(max(lst))