import sys
T = int(sys.stdin.readline())
for _ in range(T):
    lst = list(map(int, sys.stdin.readline().split()))
    s = [lst[i]+lst[i+4] for i in range(4)]
    print(max(s[0], 1) + 5 * max(s[1], 1) + 2 * max(s[2], 0) + 2 * s[3])