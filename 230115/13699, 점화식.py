import sys
n = int(sys.stdin.readline())
t = [1] + [0]*n
for i in range(n+1):
    for j in range(i):
        t[i] += t[j]*t[i-1-j]
print(t[n])