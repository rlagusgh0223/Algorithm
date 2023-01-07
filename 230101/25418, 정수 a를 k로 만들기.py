# bfs가 아닌 그냥 while로 해도 되지만 bfs알고리즘 문제니까 bfs로 만들었다
def bfs(K):
    cnt = 0
    q = deque()
    q.append(K)
    while q:
        x = q.popleft()
        if x == A:
            return cnt
        if x%2==0 and x//2>=A:
            q.append(x//2)
        else:
            q.append(x-1)
        cnt += 1

from collections import deque
import sys
A, K = map(int, sys.stdin.readline().split())
print(bfs(K))