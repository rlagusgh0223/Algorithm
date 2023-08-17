import sys
Q = int(sys.stdin.readline())
for _ in range(Q):
    a = int(sys.stdin.readline())
    if a&(-a) == a:
        print(1)
    else:
        print(0)