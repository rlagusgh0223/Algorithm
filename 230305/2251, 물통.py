def pour(x, y):
    if visit[x][y] == 0:
        visit[x][y] = 1
        q.append((x, y))

def BFS():
    q.append((0, 0))
    visit[0][0] = 1
    while q:
        x, y = q.popleft()  # A, B 물통에 들어있는 물의 양
        z = C-x-y  # C가 가득찬 상황에서 시작했으므로 총 물의 양은 C와 같다. z는 C물통의 물의 양
        if x == 0:
            ans.append(z)
        # a->b
        water = min(x, B-y)
        pour(x-water, y+water)
        # a->c
        water = min(x, C-z)
        pour(x-water, y)
        # b->a
        water = min(y, A-x)
        pour(x+water, y-water)
        # b->c
        water = min(y, C-z)
        pour(x, y-water)
        # c->a
        water = min(z, A-x)
        pour(x+water, y)
        # c->b
        water = min(z, B-y)
        pour(x, y+water)


from collections import deque
import sys
A, B, C = map(int, sys.stdin.readline().split())
q = deque()
ans = []
visit = [[0]*(B+1) for _ in range(A+1)]
BFS()
ans.sort()
print(*ans)