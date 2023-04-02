# pypy3로 제출해야 된다
def BFS(A, B):
    q = deque()
    q.append((A, ''))
    visit = [0] * 10000
    visit[A] = 1
    while q:
        now, st = q.popleft()
        if now == B:
            return st
        nxt = (now*2) % 10000
        if visit[nxt] == 0:
            visit[nxt] = 1
            q.append((nxt, st+'D'))
        nxt = (now-1) % 10000
        if visit[nxt] == 0:
            visit[nxt] = 1
            q.append((nxt, st+'S'))
        # 어차피 마지막에 10000으로 나눠주니까 10을 곱한다음에 굳이 첫자리 빼줄 필요 없다
        nxt = (now*10 + now//1000) % 10000
        if visit[nxt] == 0:
            visit[nxt] = 1
            q.append((nxt, st+'L'))
        nxt = (now//10 + (now%10)*1000) % 10000
        if visit[nxt] == 0:
            visit[nxt] = 1
            q.append((nxt, st+'R'))

from collections import deque
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(BFS(A, B))