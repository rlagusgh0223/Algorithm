import sys
N = int(sys.stdin.readline())
d = [0] * (N+1)
d[0] = 1
for i in range(2, N+1, 2):
    d[i] = d[i-2] * 3
    for j in range(i-4, -1, -2):
        d[i] += d[j] * 2
print(d[N])