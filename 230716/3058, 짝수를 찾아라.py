import sys
T = int(sys.stdin.readline())
for _ in range(T):
    num = list(map(int, sys.stdin.readline().split()))
    even = []
    for now in num:
        if now%2 == 0:
            even.append(now)
    print(sum(even), min(even))