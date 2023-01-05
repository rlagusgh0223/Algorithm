import sys
T = int(sys.stdin.readline())
for i in range(T):
    x, y, z = map(int, sys.stdin.readline().split())
    print(min(x, y, z))