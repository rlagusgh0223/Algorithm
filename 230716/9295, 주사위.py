import sys
T = int(sys.stdin.readline())
for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    print("Case {}: {}".format(i+1, x+y))