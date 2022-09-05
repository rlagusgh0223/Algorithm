N, K = map(int, input().split())

Nf = 1
for i in range(1, N+1):
    Nf *= i

Kf = 1
for i in range(1, K+1):
    Kf *= i

NKf = 1
for i in range(1, N-K+1):
    NKf *= i

print(Nf // (Kf * NKf))