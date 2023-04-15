# pypy3로 해야된다
import sys
N = int(sys.stdin.readline())
lst = []
tri = 0
i = 0
while tri < N:
    i += 1
    tri += (i * (i+1)) // 2  # 정삼각형을 구하는 점화식, 사면체는 현재까지의 정삼각형들의 합과 같다
    lst.append(tri)
dp = [300000 for _ in range(N+1)]  # N은 300000 이하이므로 이 수보다 큰 사면체 경우의 수 는 올 수 없다
for ck in range(1, N+1):
    for now in lst:
        if now == ck:
            dp[ck] = 1
            break
        elif now > ck:
            break
        dp[ck] = min(dp[ck], dp[ck-now]+1)  # now는 사면체 단위이므로 현재 포탄개수에서 사면체 개수를 뺀 곳의 사면체 개수 + 1 은 최소 사면체 개수이다
        # ex) 현재 포탄의 개수가 15라면 사면체 가능 개수는 1, 4, 10이므로
        # 1, 4, 10개가 적은 포탄인 경우의 사면체 가능 개수에 1을 더한 값 중 최솟값을 입력한다
print(dp[-1])