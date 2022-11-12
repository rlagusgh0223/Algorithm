import sys
d = [0] * 91
d[1] = 1
d[2] = 1
N = int(sys.stdin.readline())
for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]
print(d[N])