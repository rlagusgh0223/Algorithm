import sys
N, K = map(int, sys.stdin.readline().split())

nf = 1
for i in range(1, N+1):
    nf *= i

kf = 1
for i in range(1, K+1):
    kf *= i

nkf = 1
for i in range(1, N-K+1):
    nkf *= i

print(nf//(kf*nkf))