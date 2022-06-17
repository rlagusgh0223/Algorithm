def GCD(x, y):    # 최대공약수를 구하는 함수
  if y%x:
    return GCD(y%x, x)
  else:
    return x

N, M = map(int, input().split(':'))    # ':'를 기준으로 문자열을 나눠서 입력 받음
x = GCD(N, M)    # 입력받은 문자열을 최대공약수를 구하는 함수에 집어넣음
print(N//x, end='')    # 약분한 값 출력
print(':', end='')
print(M//x)