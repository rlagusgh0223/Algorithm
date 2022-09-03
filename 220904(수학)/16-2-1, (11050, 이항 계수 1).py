N, K = map(int, input().split())

np = 1
for i in range(1, N+1):
    np *= i

kp = 1
for i in range(1, K+1):
    kp *= i

nkp = 1
for i in range(1, N-K+1):
    nkp *= i

print(np//(kp*nkp))