def GCD(a, b):
    if b%a:
        return GCD(b%a, a)
    else:
        return a
import sys
n, m = map(int, sys.stdin.readline().split(":"))
answer = GCD(n, m)
print(n//answer, end='')
print(":", end='')
print(m//answer)