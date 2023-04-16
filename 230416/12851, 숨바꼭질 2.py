def BFS(N, K):
    q = deque()
    q.append(N)
    road[N] = 0
    cnt = 0
    while q:
        x = q.popleft()
        if x == K:
            cnt += 1
            continue
        for nx in (x+1, x-1, x*2):
            if 0<=nx<=100000 and (road[nx]==-1 or road[nx]==road[x]+1):  # 여기서 어차피 최소 거리를 구하므로 x==K일때 따로 조건 걸 필요가 없다
                road[nx] = road[x] + 1
                q.append(nx)
    print(road[K])
    print(cnt)

from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
road = [-1] * 100001  # 0<=N,K<=100000이니까. K+2로 하면 인덱스 에러 난다. N이 K보다 작다는 조건이 없어서 그런것 같다
BFS(N, K)