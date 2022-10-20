from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
Max = 200000
lst = [0] * (Max+1)
q = deque()
q.append(N)
while q:
    now = q.popleft()
    if now == K:  # 이 부분이 없으면 while이 엄청 돌게되서 틀렸다고 하는것 같다
        print(lst[K])
        break
    for nxt in [now-1, now+1, now*2]:
        if 0<=nxt<=Max and lst[nxt] == 0:
            lst[nxt] = lst[now] + 1
            q.append(nxt)