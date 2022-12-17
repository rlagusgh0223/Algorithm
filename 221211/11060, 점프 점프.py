import sys
N = int(sys.stdin.readline())
a = list(map(int, input().split()))
d = [-1 for _ in range(N)]
d[0] = 0
for i in range(1, N):
    for j in range(0, i):
        if d[j]!=-1 and i-j<=a[j]:
            if d[i]==-1 or d[i]>d[j]+1:
                d[i] = d[j] + 1
print(d[-1])