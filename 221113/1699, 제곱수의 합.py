import sys
N = int(sys.stdin.readline())
d = [0] * (N+1)
for i in range(1, N+1):
    d[i] = i
    j = 1
    while j*j <= i:
        if d[i] > d[i-j*j]+1:
            d[i] = d[i-j*j]+1
        j += 1
print(d[N])