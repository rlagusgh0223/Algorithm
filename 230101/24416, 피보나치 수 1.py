def fib(n):
    global cnt1
    if n==1 or n==2:
        cnt1 += 1
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonacci(n):
    global cnt2
    val = [0, 1, 1]
    if n >= 3:
        for i in range(3, n+1):
            val.append(val[i-1] + val[i-2])
            cnt2 += 1
    return val[n]

import sys
n = int(sys.stdin.readline())
cnt1 = 0
cnt2 = 0
fib(n)
fibonacci(n)
print(cnt1, cnt2)