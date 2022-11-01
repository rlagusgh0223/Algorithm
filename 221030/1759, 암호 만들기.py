def check(password):
    ja = mo = 0
    for x in password:
        if x in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja>=2 and mo>=1

def go(n, alpha, password, i):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    go(n, alpha, password+alpha[i], i+1)
    go(n, alpha, password, i+1)

import sys
L, C = map(int, sys.stdin.readline().split())
c = list(sys.stdin.readline().split())
c.sort()
go(L, c, "", 0)