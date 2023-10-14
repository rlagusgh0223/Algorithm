import sys
T = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
for now in N:
    ans = 0
    for n in range(1, now):
        if now % n == 0:
            ans += n
    if ans == now:
        print("Perfect")
    elif ans < now:
        print("Deficient")
    else:
        print("Abundant")