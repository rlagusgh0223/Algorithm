import sys

def GCD(a, b):    # 유클리드 호제법을 통한 두 수의 최대공약수를 빠르게 구하는 함수
  if b%a:
    return GCD(b%a, a)    # b%a의 값이 0이 아니라면 다시 계산
  else:
    return a    # b%a의 값이 0이라면 배수이므로 a를 리턴

N, M = map(int, sys.stdin.readline().split(':'))
a = GCD(N, M)    # N, M의 최대공약수 a를 구한다
print(N//a, end='')
print(':', end='')
print(M//a, end='')