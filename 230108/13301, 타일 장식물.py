import sys
N = int(sys.stdin.readline())
pibo = [1, 1]
plus = [0, 2]
for n in range(2, N):
    pibo.append(pibo[n-1]+pibo[n-2])
    plus.append(plus[n-1]+plus[n-2])
print(4*pibo[N-1]+plus[N-1])