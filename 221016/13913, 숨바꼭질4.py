# 백준 방식대로 했는데 런타임 에러가 나온다
from collections import deque
import sys

def search(n, m):
    if n != m:
        search(n, (form[m]))
    print(m, end = ' ')

N, K = map(int, sys.stdin.readline().split())
q = deque()
q.append(N)
Max = 200000
lst = [0] * (Max+1)
form = [0] * (Max+1)
while q:
    now = q.popleft()
    for nxt in [now-1, now+1, now*2]:
        if now == K:
            print(lst[now])
            break
        if 0<=nxt<=Max and lst[nxt] == 0:
            lst[nxt] = lst[now] + 1
            q.append(nxt)
            form[nxt] = now
search(N, K)