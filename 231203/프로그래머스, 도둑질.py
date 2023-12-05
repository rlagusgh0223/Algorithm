# 첫번째 집과 마지막 집이 연결된 형태이므로
# 첫번째 집을 훔치고 마지막 집을 훔치면 안된다
# 또한, 마지막 집을 훔치고 첫번째 집을 훔치면 안된다def solution(money):

# 코드는 아래 코드가 더 간결하지만
# dp[1]까지 직접 값을 입력하고
# 반복문을 2부터 돌리는게 조금 더 빠른것 같다
def solution(money):
    dp1 = [0] * (len(money)-1)
    dp2 = [0] * len(money)

    # 첫번째 집을 훔치는 경우
    dp1[0] = money[0]
    for i in range(1, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
        # 두번째 집의 경우 사실상 max(money[0], money[1])과 같다
        # i가 1일때 dp1은 첫번째 집을 제외하곤 다 0이기 때문이다

    # 마지막 집을 훔치는 경우
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
        # 0으로 초기화 되어 있으니 첫번째 집을 훔치지 않은 경우를 또 입력할 필요는 없다
        # i가 1일때 dp2는 모두 0이므로 두번째 집은 사실상 money[1]이 된다
    
    return max(dp1[-1], dp2[-1])


import sys
money = list(map(int, sys.stdin.readline().strip().split(", ")))
print(solution(money))