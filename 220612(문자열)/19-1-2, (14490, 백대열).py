def GCD(x, y):
  if y%x:
    return GCD(y%x, x)
  else:
    return x

N, M = map(int, input().split(':'))
a = GCD(N, M)
print(N//a, end='')
print(':', end='')
print(M//a, end='')