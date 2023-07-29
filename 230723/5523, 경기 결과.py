import sys
N = int(sys.stdin.readline())
cnt = [0, 0]
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    if A > B:
        cnt[0] += 1
    elif A < B:
        cnt[1] += 1
print(*cnt)