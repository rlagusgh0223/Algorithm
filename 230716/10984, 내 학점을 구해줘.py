import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cs, gs = 0, 0
    for i in range(N):
        C, G = map(float, sys.stdin.readline().split())
        cs += int(C)
        gs += C*G
    print("{} {:.1f}".format(cs, gs/cs))