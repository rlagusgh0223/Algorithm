N, K = list(map(int, input().split()))

up = 1
for i in range(1, N+1):  # N!을 구한다
    up *= i

down = 1
for i in range(1, N-K+1):  # (N-K)!을 구한다
    down *= i

down2 = 1
for i in range(1, K+1):  # K!을 구한다
    down2 *= i

down *= down2  # K! * (N-K)! 을 구했다

print(up//down)  # 최종식인 N! / (K! * (N-K)!) 을 구한다