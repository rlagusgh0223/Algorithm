# pypy3로 해야 된다
import sys
A, N = map(int, sys.stdin.readline().split())
K = list(map(int, sys.stdin.readline().split()))
for i in range(A, 0, -1):
    for j in range(1, i):
        if K[j-1] > K[j]:
            K[j-1], K[j] = K[j], K[j-1]
            N -= 1
            if N == 0:
                print(*K)
                exit()
print(-1)