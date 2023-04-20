def DFS(depth):
    if depth == M:
        print(*ans, sep=' ')
        return
    for i in range(N):
        ans[depth] = lst[i]  # 어차피 여기에서 값을 재정의 하므로 굳이 입력한 값을 지울 필요 없다
        DFS(depth + 1)

import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
ans = [0] * M
DFS(0)