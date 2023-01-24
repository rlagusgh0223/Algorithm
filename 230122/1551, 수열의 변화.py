import sys
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split(',')))
B = list(A)
for k in range(K):
    N -= 1
    for i in range(N):
        B[i] = B[i+1] - B[i]
    B.pop()
print(*B,sep=',')