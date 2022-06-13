import sys
N, M = map(int, sys.stdin.readline().split(':'))

def GCD(x, y):
  if y%x:
    return GCD(y%x, x)
  else:
    return x

a = GCD(N, M)
print(N//a, end='')
print(":", end='')
print(M//a, end='')