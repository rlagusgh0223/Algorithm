import sys
N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))
D = [-1] * (N+1)
D[0] = 0
for i in range(1, N+1):
    for j in range(1, i+1):
        if D[i]==-1 or D[i]>D[i-j]+P[j]:
            D[i] = D[i-j] + P[j]
print(D[N])