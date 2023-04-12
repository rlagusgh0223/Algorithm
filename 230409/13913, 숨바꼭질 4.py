# BFS에서 이동한 위치를 저장하면 메모리 초과나므로
# check에서 각각 이전값만 저장하고 역순으로 출력하게 해야된다
def move(now):
    ans = []
    temp = now
    for _ in range(visit[now]+1):
        ans.append(temp)
        temp = check[temp]
    print(*ans[::-1])

def BFS(N, K):
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(visit[x])
            move(x)
            return
        for nxt in (x-1, x+1, x*2):
            if 0<=nxt<=100000 and visit[nxt]==0:
                visit[nxt] = visit[x] + 1
                check[nxt] = x
                q.append(nxt)

from collections import deque
import sys
visit = [0] * 100001
check = [0] * 100001
N, K = map(int, sys.stdin.readline().split())
BFS(N, K)