import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
ck = [lst[0], 0]
for now in lst:
    ck[0] = min(ck[0], now)
    ck[1] = max(ck[1], now-ck[0])
print(ck[1])