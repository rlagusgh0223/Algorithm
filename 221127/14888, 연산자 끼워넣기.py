def calc(a, index, cur, plus, minus, mul, div):
    if len(a) == index:
        return cur, cur
    res = []
    if plus > 0:
        res.append(calc(a, index+1, cur+a[index], plus-1, minus, mul, div))
    if minus > 0:
        res.append(calc(a, index+1, cur-a[index], plus, minus-1, mul, div))
    if mul > 0:
        res.append(calc(a, index+1, cur*a[index], plus, minus, mul-1, div))
    if div > 0:
        if cur >= 0:
            res.append(calc(a, index+1, cur//a[index], plus, minus, mul, div-1))
        else:
            res.append(calc(a, index+1, -(-cur//a[index]), plus, minus, mul, div-1))
    ans = (
        max(t[0] for t in res),
        min(t[1] for t in res)
    )
    return ans

import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
plus, minus, mul, div = map(int, sys.stdin.readline().split())
ans = calc(A, 1, A[0], plus, minus, mul, div)
print(ans[0])
print(ans[1])