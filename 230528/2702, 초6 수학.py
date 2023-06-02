# 최대공약수
# a, b 작은 숫자부터 1까지 반복문을 이용해서 나누는데
# a, b 모두 나누어 떨어지면 최대공약수

# 최소공배수
# a, b 중 더 큰 숫자부터 a*b까지 반복문을 이용해서 나누는데
# 해당 수가 a, b에 모두 나누어 떨어지면 최소 공배수
# 유클리우드 호제법
# A%B==0이 되는 순간 B는 최대공약수가 된다
# 최소공배수는 a*b//최대공약수 이다
def abmin(a, b):
    A = max(a, b)
    B = min(a, b)
    while A%B != 0:
        A, B = B, A%B
    return B

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    gcd = abmin(a, b)
    print(a*b//gcd, gcd)