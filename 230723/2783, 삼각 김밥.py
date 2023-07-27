import sys
X, Y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
lst = [X/Y] * (N + 1)
for i in range(1, N+1):
    x, y = map(int, sys.stdin.readline().split())
    lst[i] = x / y
print("{:.2f}".format(min(lst) * 1000))