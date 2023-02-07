import sys
A, B = map(int, sys.stdin.readline().split())
print(str(A//B)+'.', end='')
i = 0
while A%B and i<1000:
    A = A%B * 10
    i += 1
    print(A//B, end='')
print()