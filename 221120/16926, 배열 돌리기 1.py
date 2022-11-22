# A[k][j]    k <= j < M-1-k
# A[i][M-1-k]    k <= i < N-1-k
# A[N-1-k][j]    k <= j < M-1-k
# A[i][k]    k <= i < N-1-k

import sys
N, M ,R = map(int, sys.stdin.readline().split())
A = []
groups = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
gn = min(N, M)//2
for k in range(gn):
    group = []
    for j in range(k, M-1-k):
        group.append(A[k][j])
    for i in range(k, N-1-k):
        group.append(A[i][M-1-k])
    for j in range(M-1-k, k, -1):
        group.append(A[N-1-k][j])
    for i in range(N-1-k, k, -1):
        group.append(A[i][k])
    groups.append(group)

for k in range(gn):
    group = groups[k]
    l = len(group)
    index = R%l
    for j in range(k, M-1-k):
        A[k][j] = group[index]
        index = (index+1)%l
    for i in range(k, N-1-k):
        A[i][M-1-k] = group[index]
        index = (index+1) % l
    for j in range(M-1-k, k, -1):
        A[N-1-k][j] = group[index]
        index = (index+1) % l
    for i in range(N-1-k, k, -1):
        A[i][k] = group[index]
        index = (index+1) % l

for row in A:
    print(' '.join(map(str, row)))