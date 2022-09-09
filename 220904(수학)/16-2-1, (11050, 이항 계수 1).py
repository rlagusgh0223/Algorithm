import sys
N, K = map(int, sys.stdin.readline().split())
Nf = Kf = NKf = 1
for i in range(1, N+1):
    Nf *= i
for i in range(1, K+1):
    Kf *= i
for i in range(1, N-K+1):
    NKf *= i
print(Nf//(Kf * NKf))