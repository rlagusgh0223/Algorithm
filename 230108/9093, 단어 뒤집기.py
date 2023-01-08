import sys
T = int(sys.stdin.readline())
for i in range(T):
    lst = list(sys.stdin.readline().split())
    for now in lst:
        print(now[::-1], end=' ')
    print()