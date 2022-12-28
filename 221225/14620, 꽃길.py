def ck(lst):
    flow = []
    ret = 0
    for flower in lst:
        x = flower // N
        y = flower % N
        if x<=0 or x>=N-1 or y<=0 or y>=N-1:
            return 10000
        for w in range(5):
            flow.append((x+dx[w], y+dy[w]))
            ret += G[x+dx[w]][y+dy[w]]
    if len(set(flow)) != 15:
        return 10000
    return ret

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
ans = 10000
dx = [0, 0, 1, 0, -1]
dy = [0, 1, 0, -1, 0]
for i in range(N*N):
    for j in range(i+1, N*N):
        for k in range(j+1, N*N):
            ans = min(ans, ck((i,j,k)))
print(ans)