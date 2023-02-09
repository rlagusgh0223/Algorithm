import sys
while True:
    cnt = 0
    try:
        N, B, M = map(float, sys.stdin.readline().split())
        B *= 0.01
        while N <= M:
            N += N*B
            cnt += 1
        print(cnt)
    except:
        break