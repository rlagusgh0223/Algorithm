import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
D = [1] * N
V = [-1] * N
for i in range(N):
    for j in range(i):
        if A[j]<A[i] and D[j]+1>D[i]:
            D[i] = D[j] + 1
            V[i] = j
ans = max(D)
p = [i for i, x in enumerate(D) if x==ans][0]
print(ans)
def go(p):
    if p == -1:
        return
    go(V[p])
    print(A[p], end=' ')
go(p)
print()