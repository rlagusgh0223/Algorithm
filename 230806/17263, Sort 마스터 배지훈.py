import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
print(A[-1])