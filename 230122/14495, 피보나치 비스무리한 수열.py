import sys
n = int(sys.stdin.readline())
f = [0, 1, 1, 1] + [0]*(n-3)
for i in range(4, n+1):
    f[i] = f[i-1]+f[i-3]
print(f[n])