n, m = map(int, input().split(':'))

def GCD(x, y):
  if y%x:
    return GCD(y%x, x)
  else:
    return x

a = GCD(n, m)
print(n//a, end='')
print(':', end='')
print(m//a, end='')