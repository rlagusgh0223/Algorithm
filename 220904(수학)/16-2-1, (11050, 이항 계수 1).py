N, K = map(int, input().split())
Nf = Kf = NKf = 1
for i in range(2, N+1):
    Nf *= i
for i in range(2, K+1):
    Kf *= i
for i in range(2, N-K+1):
    NKf *= i

print(Nf//(Kf * NKf))