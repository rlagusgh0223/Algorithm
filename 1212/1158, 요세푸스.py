from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
man = deque()
res = []
for i in range(1,n+1):
    man.append(i)

while man:
    for i in range(m):
        if i == m-1:
            out = man.popleft()
            res.append(out)
        else:
            out = man.popleft()
            man.append(out)

print('<',end='')
for i in range(len(res)):
    if i == len(res)-1:
        print(res[i],end='')
    else:
        print(res[i],end=', ')
print('>')