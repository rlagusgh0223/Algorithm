# 무슨 원리인지는 모르겠는데 DFS에서 cnt를 받는 방식DFS(start, cnt)은 틀렸다고 하고
# cnt를 전역변수로 만든 다음 따로 계산해야 맞았다고 한다
def DFS(start):
    global cnt
    ck[start] = cnt
    for nxt in num[start]:
        if ck[nxt] == 0:
            cnt += 1
            DFS(nxt)

import sys
sys.setrecursionlimit(10**6)  # 재귀함수 깊이 지정하는 함수
N, M, R = map(int, sys.stdin.readline().split())
num = [[] for _ in range(N+1)]
ck = [0] * (N+1)
cnt = 1
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    num[u].append(v)
    num[v].append(u)
for i in range(N+1):
    num[i].sort(reverse=True)
DFS(R)
for i in range(1, N+1):
    print(ck[i])