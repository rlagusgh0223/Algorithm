from math import factorial
import sys
N = int(sys.stdin.readline())
num = N
fact = [factorial(i) for i in range(21)]  # 입력되는 N은 20!이하이다
for i in range(20, -1, -1):
    if num >= fact[i]:
        num -= fact[i]
print("YES" if N!=0 and num==0 else "NO")