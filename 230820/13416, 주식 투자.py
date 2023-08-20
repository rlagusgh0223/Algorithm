import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    money = 0
    for _ in range(N):
        A, B, C = map(int, sys.stdin.readline().split())
        now = max(A, B, C)
        if now > 0:
            money += now
    print(money)