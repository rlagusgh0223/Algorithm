import sys
T, W = map(int, sys.stdin.readline().split())
plum = [int(sys.stdin.readline()) for _ in range(T)]
dp = [[0]*(W+1) for _ in range(T+1)]
for i in range(1, T+1):
    # 자두가 다 떨어질 때까지 한번도 움직이지 않은 경우
    if plum[i-1] == 1:  # 1의 위치에서 자두가 떨어지면
        dp[i][0] = dp[i-1][0] + 1
    else:  # 2의 위치에서 자두가 떨어지면
        dp[i][0] = dp[i-1][0]
    # 한번 이상 움직인 경우
    for j in range(1, W+1):
        # 자두가 떨어지는 위치와 현재 위치가 같은 경우 자두를 얻을 수 있다
        # 이전 위치에서 이동해서 먹을것인지, 그 위치 그대로 먹을것인지 더 많이 먹을 수 있는 위치로 정한다 
        if (plum[i-1]==1 and j%2==0) or (plum[i-1]==2 and j%2==1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        # 자두가 떨어지는 위치에 없다면 자두는 못먹는다
        # 다만 이전 위치와 현재 위치 중 더 많이 먹을 수 있는 경우를 저장한다
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[T]))