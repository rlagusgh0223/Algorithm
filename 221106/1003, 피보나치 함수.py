def fibo(n):
    if n==0:
        return memo[0]
    elif n==1:
        return memo[1]
    else:
        if memo[n][0]>0 or memo[n][1]>0:
            return memo[n]
        x1, y1 = fibo(n-1)
        x2, y2 = fibo(n-2)
        memo[n] =[x1+x2, y1+y2]
        return memo[n]

import sys
T = int(sys.stdin.readline())
for i in range(T):
    memo = [[0, 0]] * 41
    memo[0] = [1, 0]
    memo[1] = [0, 1]
    now = int(sys.stdin.readline())
    zero, one = fibo(now)
    print(zero, one)