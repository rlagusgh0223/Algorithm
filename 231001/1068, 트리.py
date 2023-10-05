def DFS(now):
    tree[now] = -2  # 지운 노드는 -2로 표시한다
    for i in range(N):
        if tree[i] == now:  # 지운 노드를 부모로 삼고 있는 노드가 있다면
            DFS(i)  # 들어가서 마저 지운다(-2로 표시)

import sys
N = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
delete = int(sys.stdin.readline())
cnt = 0
DFS(delete)
for i in range(N):
    # 지운 노드가 아니고 지금 노드를 부모로 삼고 있는 노드가 없다면 1 증가
    if tree[i]!=-2 and not i in tree:
        cnt += 1
print(cnt)