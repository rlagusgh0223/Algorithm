import sys
n = int(sys.stdin.readline())
x, y, z = 0, 1, 1
for i in range(n):
    x = y%1000000007
    y = z%1000000007
    z = x+y
print(x)