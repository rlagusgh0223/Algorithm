def solution(money):
    # 원으로 집이 배치되어 있으며
    # 인접한 두 집을 털 수 없으므로
    # 첫번째 집을 턴다면 마지막 집은 털 수 없다
    # dp1은 첫번째 집을 털고 마지막 집을 털지 않은 경우
    # dp2는 첫번째 집을 털지 않고 마지막 집을 턴 경우 이다
    dp1, dp2 = [0]*len(money), [0]*len(money)
    dp1[0] = money[0]
    for i in range(1, len(money)):
        # dp가 0으로 초기화 되어 있어서
        # i가 1이어도 dp[-1]+money[1]이 되어 0+money[1]이므로
        # 계산에 영향을 주지 않는다
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
    # dp1[-1]은 마지막 집을 턴 결과니까 -2의 값으로 계산한다
    return max(dp1[-2], dp2[-1])

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
