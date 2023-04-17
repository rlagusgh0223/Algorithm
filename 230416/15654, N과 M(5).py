# 문제에서는 중복된 값만 나오지 않으면 된다고 했다
# M개의 문자열 중에 숫자의 순서는 상관없다
# 다만, 숫자열의 크기가 오름차순이어야 한다
def DFS(depth):
    if depth == M:
        print(*ans, sep=' ')
        return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            ans[depth] = lst[i]
            DFS(depth+1)
            visit[i] = 0

import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
visit = [0] * N  # 중복된 값이 나오지 않도록 체크
ans = [0] * M
DFS(0)