import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
V = int(sys.stdin.readline())
ans = 0
for now in lst:
    if now == V:
        ans += 1
print(ans)