import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
d1 = [0] * N
d2 = [0] * N
for i in range(N):
    d1[i] = 1
    for j in range(i):
        if A[j]<A[i] and d1[i]<d1[j]+1:
            d1[i] = d1[j]+1
for i in range(N-1, -1, -1):
    d2[i] = 1
    for j in range(i+1, N):
        if A[j]<A[i] and d2[i]<d2[j]+1:
            d2[i] = d2[j]+1
d = [d1[i]+d2[i]-1 for i in range(N)]
print(max(d))