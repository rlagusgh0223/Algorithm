import sys
def GCD(x, y):
  if y%x:
    return GCD(y%x, x)
  else:
    return x
    
N, M = map(int, sys.stdin.readline().split(':'))
a = GCD(N, M)
print(N//a, end='')
print(':', end='')
print(M//a, end='')