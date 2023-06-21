import sys
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
if A+B >= 2*C:
    print((A+B)-(2*C))
else:
    print(A+B)