import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    cnt = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            # 계산을 하고 정수인지 아닌지 판단하면 시간초과 나온다
            if (a**2+b**2+m) % (a*b) == 0:
                cnt += 1
    print(cnt)