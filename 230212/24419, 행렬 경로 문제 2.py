from math import factorial
import sys
n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print((factorial(2*n)//(factorial(n)**2))%1000000007, n**2)