import sys
T = int(sys.stdin.readline())
for _ in range(T):
    lst = list(sys.stdin.readline().rstrip())
    print(lst[0], lst[-1], sep='')