import sys
A, B, C, M = map(int, sys.stdin.readline().split())
state = work = 0
if A > M:
    print(0)
    exit()
for _ in range(24):
    if state+A > M:
        if state-C < 0:
            state = 0
        else:
            state -= C
    else:
        state += A
        work += B
print(work)