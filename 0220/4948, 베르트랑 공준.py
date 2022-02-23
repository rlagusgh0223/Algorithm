# 지속적인 공부 필요
from math import sqrt
import sys
result = []

def sosu(a, b):
    cnt = 0
    check = [True] * (b+1)

    for i in range(2, int(sqrt(b) + 1)):
        if check[i] == True:
            for j in range(i*2, b+1, i):
                check[j] = False
    
    for i in range(a+1, b+1):
        if check[i] == True:
            cnt += 1
    return cnt

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    result.append(sosu(n, 2*n))

for i in result:
    print(i)