# 카탈란 수
# 1. 잘 짜인 괄호
# 2. 산 만들기
# 3. 대각선 피해가기
# 4. 다각형을 삼각형으로 나누기
# 에 쓸 수 있는 것 같다
# 점화식 = 2n! / (n! * (n+1)!)
import sys, math

def catalan(n):
    return math.factorial(2 * n) // (math.factorial(n) * math.factorial(n + 1))

T = int(sys.stdin.readline())
for _ in range(T):
    L = int(sys.stdin.readline())
    if L % 2 == 1:  # 홀수인 경우에는 어떻게든 완벽한 괄호가 나올 수 없다
        print(0)
    else:
        print(catalan(L//2) % 1000000007)  # 문제에서 주어진 대로 답이 나오기 위해서는 2로 나눈 값을 줘야 되지만 왜 이렇게 되는지는 모르겠다