import sys
n, m = map(int, sys.stdin.readline().split())
a = 100 - n
b = 100 - m
c = 100 - (a+b)
d = a * b
q = d // 100
r = d % 100
print(a, b, c, d, q, r)
print(c+q, r)