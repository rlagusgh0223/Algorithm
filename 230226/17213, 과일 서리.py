import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
dp = [[1], [1]*(M-N+1)]  # 과일의 종류가 1개, 2개인 경우
# 과일 종류가 2개인 경우 경우의 수는 M-1이된다.
# M :    2 3 4 5 6 7
# 경우 : 1 2 3 4 5 6
# dp에는 N과M의 개수가 같을때부터 입력되므로 dp[1]의 값이 모두 1이면
# 답을 출력할때 sum을 이용해서 경우의 수가 나온다
for i in range(2, N):  # 과일의 종류가 3개 이상인 경우
    dp.append([sum(dp[i-1][:j+1]) for j in range(M-N+1)])
    # N=2 일때
    # M:경우의수    ->  2:1       3:2          4:3            5:4               6:5
    # N=3일때
    # M:경우의수    ->  3:1       4:3(1+2)     5:6(1+2+3)     6:10(1+2+3+4)
    # 이전 과일의 종류[i-1]에서 현재 과일의 개수 전까지 합[:j+1]이 지금 과일의 종류와 과일의 개수이다
    # j+1이지만 N이 1 증가해서 M-N을 반영한 값도 1 증가했으므로 이전까지의 값이 된다
    # ex. N=2일때 dp[1][0]값은 M=2일때 값이지만, N=3일때 dp[2][0]값은 M=3이다.
    # i-1에서 j보다 작은 경우에 남은 과일의 개수를 마지막 과일의 종류에 넣는다고 가정하면 이전 경우들의 수의 합으로 나온다.
    # i-1에서 과일의 수가 같은 경우는 이미 다 분배되어 더 추가할 수 없기 때문에 제외한다.
print(sum(dp[N-1]))