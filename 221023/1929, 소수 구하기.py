# 에라토스테네스의 체
import sys
MAX = 1000000
check = [True for _ in range(MAX+1)]
check[0] = check[1] = False
for i in range(2, MAX+1):
    if check[i]:
        j = i+i
        while j <= MAX:
            check[j] = False
            j += i

M, N = map(int, sys.stdin.readline().split())
for i in range(M, N+1):
    if check[i]:
        print(i)