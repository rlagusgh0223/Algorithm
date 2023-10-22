def DFS(r):
    check[r] = 1
    for i in tree[r]:
        if check[i] == 0:
            DFS(i)
            check[r] += check[i]

import sys
sys.setrecursionlimit(10**9)
N, R, Q = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N+1)]
check = [0] * (N+1)
for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    tree[U].append(V)
    tree[V].append(U)

DFS(R)

for _ in range(Q):
    u = int(sys.stdin.readline())
    print(check[u])