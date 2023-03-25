import sys
N = int(sys.stdin.readline())
dp = [1, 1, 2] + [0]*(38)  # N의 개수는 40까지다. 0번째 자리는 vip 마지막 좌석이 N이 될 경우 결과값에 영향을 주지 않기 위해 1을 줬다(N+1 -N -1 = 0)
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]  # 점화식
M = int(sys.stdin.readline())
vip = [int(sys.stdin.readline()) for _ in range(M)]+[N+1]
# ex)
# N=9, vip의 마지막 입력값이 9이면 마지막 연산에서dp = 10 -9 -1 = 0이 되므로 1을 곱해 최종값에 영향을 주지 않게 한다
# vip값이 없을땐 vip=10이 되고 10-0-1 의 값 dp[9]의 값이 출력된다
# vip의 마지막 값이 9보다 작을땐 마지막값과 10 사이의 칸 수만큼 계산된다
# vip 마지막 값 7이면 10-7-1 = 2(8번째, 9번째 좌석) dp[2]의 값 만큼 계산됨
ans, cnt = 1, 0
for now in vip:
    ans *= dp[now - cnt - 1]
    cnt = now
print(ans)