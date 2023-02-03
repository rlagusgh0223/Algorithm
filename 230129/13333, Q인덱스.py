import sys
n = int(sys.stdin.readline())
ICPC = sorted(list(map(int, sys.stdin.readline().split())))
for k in range(n, -1, -1):
    if k <= ICPC[-k]:
        print(k)
        break