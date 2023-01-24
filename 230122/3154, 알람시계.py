def effort(x, y):
    for i in range(4):
        for j in range(3):
            if button[i][j] == x:
                xa, ya = i, j
            if button[i][j] == y:
                xb, yb = i, j
    return abs(xa-xb) + abs(ya-yb)

import sys
A, B = map(int, sys.stdin.readline().split(":"))
x = B
button = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
now = 1000
while A<=99:
    B = x
    a, b = A//10, A%10
    while B<=99:
        c, d = B//10, B%10
        e = effort(a,b)+effort(b,c)+effort(c,d)
        if now > e:
            now = e
            ck = [a,b,':',c,d]
        B += 60
    A += 24
print(*ck,sep="")