# 이동거리 = 속도 * (연료량/연료소비율)
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, D = map(int, sys.stdin.readline().split())
    cnt = 0
    for _ in range(N):
        v, f, c = map(int, sys.stdin.readline().split())
        if D <= (v * (f / c)):
            cnt += 1
    print(cnt)