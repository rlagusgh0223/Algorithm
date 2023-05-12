def DFS(depth, weigth):
    global cnt
    if depth == N:
        cnt += 1
        return
    for i in range(N):
        if check[i] or weigth+A[i]-K<0: # 이미 계산한 적 있는 기구거나 현재 몸무게가 음수이면(500보다 낮아지면)
            continue
        check[i] = 1
        DFS(depth+1, weigth+A[i]-K)
        check[i] = 0

import sys
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
check = [0]*N
cnt = 0
DFS(0, 0)
print(cnt)