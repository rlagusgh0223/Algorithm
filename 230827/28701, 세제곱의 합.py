import sys
N = int(sys.stdin.readline())
A, B = 0, 0
for i in range(1, N+1):
    A += i
    B += i**3
print(A)
print(A*A)
print(B)